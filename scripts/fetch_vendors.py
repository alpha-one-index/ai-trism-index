#!/usr/bin/env python3
"""
fetch_vendors.py — AI TRiSM Market Index data fetcher
Fetches live vendor status, funding, and regulatory updates.
Uses stdlib only (urllib.request). Works in GitHub Actions.

Repository: https://github.com/alpha-one-index/ai-trism-index
License: MIT
"""

import json
import logging
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
DATA_DIR = REPO_ROOT / "data"
HISTORY_DIR = DATA_DIR / "history"
VENDORS_FILE = DATA_DIR / "vendors.json"
REGULATORY_FILE = DATA_DIR / "regulatory-tracker.json"

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT", "15"))
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", "3"))
RETRY_DELAY = float(os.environ.get("RETRY_DELAY", "2.0"))
USER_AGENT = (
    "Mozilla/5.0 (compatible; AI-TRiSM-Index-Bot/1.0; "
    "+https://github.com/alpha-one-index/ai-trism-index)"
)

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    stream=sys.stdout,
)
logger = logging.getLogger("fetch_vendors")


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def http_get(url: str, timeout: int = REQUEST_TIMEOUT) -> tuple[int, str]:
    """Fetch a URL with retries. Returns (status_code, body_text)."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/json,*/*",
        "Accept-Language": "en-US,en;q=0.9",
    }
    req = urllib.request.Request(url, headers=headers)
    last_exc = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                body = resp.read().decode("utf-8", errors="replace")
                logger.debug("GET %s \u2192 %d (%d bytes)", url, resp.status, len(body))
                return resp.status, body
        except urllib.error.HTTPError as e:
            logger.warning("Attempt %d/%d: HTTP %d for %s", attempt, MAX_RETRIES, e.code, url)
            last_exc = e
            if e.code in (403, 404, 410):
                # No point retrying permanent errors
                return e.code, ""
        except urllib.error.URLError as e:
            logger.warning("Attempt %d/%d: URL error for %s: %s", attempt, MAX_RETRIES, url, e.reason)
            last_exc = e
        except Exception as e:  # noqa: BLE001
            logger.warning("Attempt %d/%d: unexpected error for %s: %s", attempt, MAX_RETRIES, url, e)
            last_exc = e

        if attempt < MAX_RETRIES:
            time.sleep(RETRY_DELAY * attempt)

    logger.error("All %d retries failed for %s: %s", MAX_RETRIES, url, last_exc)
    return -1, ""


def is_url_live(url: str) -> bool:
    """Return True if the URL returns a 2xx or 3xx status."""
    code, _ = http_get(url)
    return 200 <= code < 400


# ---------------------------------------------------------------------------
# Vendor status checks
# ---------------------------------------------------------------------------

ACQUISITION_INDICATORS = [
    "acquired", "acquisition", "now part of", "integrated into",
    "merged with", "combining with", "joining forces",
]

FUNDING_INDICATORS = [
    r"\$[\d,.]+\s*(?:million|billion|M|B)\b",
    r"series [a-e]",
    r"seed round",
    r"growth round",
    r"raises?",
    r"funding",
    r"investment",
]


def check_vendor_website(vendor: dict) -> dict:
    """Check a vendor's website for liveness and news indicators."""
    url = vendor.get("website", "")
    if not url or url.startswith("N/A"):
        return {"website_live": None, "checked_at": _now_iso()}

    logger.info("Checking vendor site: %s (%s)", vendor.get("name"), url)
    code, body = http_get(url)
    live = 200 <= code < 400

    result = {
        "website_live": live,
        "http_status": code,
        "checked_at": _now_iso(),
    }

    if live and body:
        body_lower = body.lower()
        # Check for acquisition signals in page text
        acquisition_signals = [kw for kw in ACQUISITION_INDICATORS if kw in body_lower]
        if acquisition_signals:
            result["acquisition_signals"] = acquisition_signals
            logger.info("  \u26a0 Acquisition signal(s) found at %s: %s", url, acquisition_signals)

        # Check for recent funding mentions
        funding_mentions = []
        for pattern in FUNDING_INDICATORS:
            matches = re.findall(pattern, body_lower)
            if matches:
                funding_mentions.extend(matches[:2])
        if funding_mentions:
            result["funding_mentions"] = list(set(funding_mentions))[:5]

    return result


# ---------------------------------------------------------------------------
# Regulatory update checks
# ---------------------------------------------------------------------------

REGULATORY_SOURCES = [
    {
        "id": "eu-ai-act",
        "url": "https://artificialintelligenceact.eu/",
        "check_terms": ["enforcement", "compliance", "deadline", "august 2026", "february 2025"],
    },
    {
        "id": "nist-ai-rmf",
        "url": "https://www.nist.gov/artificial-intelligence",
        "check_terms": ["ai rmf", "600-1", "framework", "update"],
    },
    {
        "id": "iso-42001",
        "url": "https://www.iso.org/standard/81230.html",
        "check_terms": ["42001", "amendment", "revision", "2024"],
    },
]


def check_regulatory_sources() -> list[dict]:
    """Check regulatory source pages for update signals."""
    results = []
    for source in REGULATORY_SOURCES:
        logger.info("Checking regulatory source: %s", source["id"])
        code, body = http_get(source["url"])
        live = 200 <= code < 400
        found_terms = []
        if live and body:
            body_lower = body.lower()
            found_terms = [t for t in source["check_terms"] if t in body_lower]
        results.append({
            "id": source["id"],
            "url": source["url"],
            "reachable": live,
            "checked_at": _now_iso(),
            "found_terms": found_terms,
        })
    return results


# ---------------------------------------------------------------------------
# JSON load/save helpers
# ---------------------------------------------------------------------------

def load_json(path: Path) -> dict | list:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict | list, path: Path, indent: int = 2) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)
    logger.info("Saved %s (%d bytes)", path, path.stat().st_size)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Archive helpers
# ---------------------------------------------------------------------------

def archive_snapshot(source_path: Path) -> Path:
    """Copy source_path to history/stem-YYYY-MM-DD.json."""
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    dest = HISTORY_DIR / f"{source_path.stem}-{today}.json"
    shutil.copy2(source_path, dest)
    logger.info("Archived snapshot to %s", dest)
    return dest


# ---------------------------------------------------------------------------
# Fetch summary report
# ---------------------------------------------------------------------------

def build_fetch_report(
    vendor_checks: list[dict],
    regulatory_checks: list[dict],
    started_at: str,
) -> dict:
    checked = len(vendor_checks)
    live_count = sum(1 for v in vendor_checks if v.get("website_live") is True)
    down_count = sum(1 for v in vendor_checks if v.get("website_live") is False)
    acquired_signals = sum(1 for v in vendor_checks if v.get("acquisition_signals"))

    return {
        "generated_at": _now_iso(),
        "started_at": started_at,
        "summary": {
            "vendors_checked": checked,
            "websites_live": live_count,
            "websites_unreachable": down_count,
            "acquisition_signals_detected": acquired_signals,
        },
        "vendor_checks": vendor_checks,
        "regulatory_checks": regulatory_checks,
    }


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def update_vendors_json(vendor_checks: list[dict]) -> None:
    """Merge website-check results back into vendors.json metadata."""
    if not VENDORS_FILE.exists():
        logger.warning("vendors.json not found at %s, skipping update", VENDORS_FILE)
        return

    data = load_json(VENDORS_FILE)
    data["metadata"]["last_updated"] = _now_iso()
    data["metadata"]["last_fetch_checks"] = len(vendor_checks)
    data["metadata"]["last_fetch_live_count"] = sum(
        1 for v in vendor_checks if v.get("website_live") is True
    )

    # Build lookup for quick update
    check_lookup = {v["name"]: v for v in vendor_checks if "name" in v}

    categories = data.get("categories", {})
    for cat_key, category in categories.items():
        for vendor in category.get("vendors", []):
            name = vendor.get("name", "")
            if name in check_lookup:
                check = check_lookup[name]
                vendor.setdefault("_fetch_meta", {})
                vendor["_fetch_meta"]["last_checked"] = check.get("checked_at")
                vendor["_fetch_meta"]["website_live"] = check.get("website_live")
                if check.get("http_status"):
                    vendor["_fetch_meta"]["http_status"] = check["http_status"]
                if check.get("acquisition_signals"):
                    vendor["_fetch_meta"]["acquisition_signals"] = check["acquisition_signals"]
                    logger.warning(
                        "ALERT: Acquisition signals for %s \u2014 manual review recommended", name
                    )

    save_json(data, VENDORS_FILE)


def update_regulatory_json(regulatory_checks: list[dict]) -> None:
    """Update regulatory-tracker.json with source reachability data."""
    if not REGULATORY_FILE.exists():
        logger.warning("regulatory-tracker.json not found at %s, skipping", REGULATORY_FILE)
        return

    data = load_json(REGULATORY_FILE)
    data["metadata"]["last_updated"] = _now_iso()

    check_lookup = {c["id"]: c for c in regulatory_checks}
    for reg in data.get("regulations", []):
        reg_id = reg.get("id", "")
        if reg_id in check_lookup:
            check = check_lookup[reg_id]
            reg.setdefault("_fetch_meta", {})
            reg["_fetch_meta"]["last_checked"] = check.get("checked_at")
            reg["_fetch_meta"]["source_reachable"] = check.get("reachable")
            reg["_fetch_meta"]["found_terms"] = check.get("found_terms", [])

    save_json(data, REGULATORY_FILE)


def gather_all_vendors() -> list[dict]:
    """Extract flat list of all vendors from vendors.json for checking."""
    if not VENDORS_FILE.exists():
        return []
    data = load_json(VENDORS_FILE)
    vendors = []
    for category in data.get("categories", {}).values():
        for vendor in category.get("vendors", []):
            vendors.append({
                "name": vendor.get("name"),
                "website": vendor.get("website"),
                "status": vendor.get("status", "Active"),
            })
    return vendors


def main() -> int:
    started_at = _now_iso()
    logger.info("=== AI TRiSM Market Index \u2014 fetch_vendors.py ===")
    logger.info("Started at %s", started_at)

    # Ensure data directories exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    # Archive current state before any changes
    if VENDORS_FILE.exists():
        archive_snapshot(VENDORS_FILE)
    if REGULATORY_FILE.exists():
        archive_snapshot(REGULATORY_FILE)

    # Collect all vendor websites to check
    all_vendors = gather_all_vendors()
    logger.info("Found %d vendors to check", len(all_vendors))

    # Run vendor website checks
    vendor_checks = []
    for vendor in all_vendors:
        # Skip obviously acquired/integrated vendors that no longer have standalone sites
        status = vendor.get("status", "Active")
        if status == "Acquired":
            logger.debug("Skipping acquired vendor %s", vendor.get("name"))
            vendor_checks.append({
                "name": vendor["name"],
                "website": vendor.get("website"),
                "website_live": None,
                "checked_at": _now_iso(),
                "skip_reason": "acquired",
            })
            continue

        check = check_vendor_website(vendor)
        check["name"] = vendor["name"]
        vendor_checks.append(check)

        # Polite delay between requests
        time.sleep(0.5)

    # Run regulatory source checks
    regulatory_checks = check_regulatory_sources()

    # Update JSON files with check results
    update_vendors_json(vendor_checks)
    update_regulatory_json(regulatory_checks)

    # Write fetch report
    report = build_fetch_report(vendor_checks, regulatory_checks, started_at)
    report_path = DATA_DIR / "fetch-report.json"
    save_json(report, report_path)

    # Print summary
    summary = report["summary"]
    logger.info("=== Fetch Complete ===")
    logger.info("  Vendors checked:          %d", summary["vendors_checked"])
    logger.info("  Websites live:            %d", summary["websites_live"])
    logger.info("  Websites unreachable:     %d", summary["websites_unreachable"])
    logger.info("  Acquisition signals:      %d", summary["acquisition_signals_detected"])

    if summary["acquisition_signals_detected"] > 0:
        logger.warning(
            "\u26a0 %d vendor(s) have acquisition signals \u2014 review fetch-report.json",
            summary["acquisition_signals_detected"],
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())

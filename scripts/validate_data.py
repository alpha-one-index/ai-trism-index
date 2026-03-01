#!/usr/bin/env python3
"""
validate_data.py — AI TRiSM Market Index data validator
Validates JSON schemas, URL health, data ranges, and date formats.

Usage:
    python scripts/validate_data.py              # Interactive, human-readable output
    python scripts/validate_data.py --ci         # Exit non-zero on failures (CI mode)
    python scripts/validate_data.py --json       # Output results as JSON
    python scripts/validate_data.py --check urls # Run only URL health checks
    python scripts/validate_data.py --check schema  # Run only schema checks

Repository: https://github.com/alpha-one-index/ai-trism-index
License: MIT
"""

import argparse
import json
import logging
import os
import re
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
VENDORS_FILE = DATA_DIR / "vendors.json"
MARKET_DATA_FILE = DATA_DIR / "market-data.json"
REGULATORY_FILE = DATA_DIR / "regulatory-tracker.json"
VALIDATION_REPORT_FILE = DATA_DIR / "validation-report.json"

REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT", "10"))
MAX_URL_CHECKS = int(os.environ.get("MAX_URL_CHECKS", "50"))
USER_AGENT = (
    "Mozilla/5.0 (compatible; AI-TRiSM-Index-Validator/1.0; "
    "+https://github.com/alpha-one-index/ai-trism-index)"
)
GITHUB_ISSUE_LABELS = ["data-validation", "automated"]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    stream=sys.stdout,
)
logger = logging.getLogger("validate_data")

# ---------------------------------------------------------------------------
# Issue tracking
# ---------------------------------------------------------------------------

issues: list[dict] = []
warnings_list: list[dict] = []


def add_issue(
    severity: str,
    category: str,
    message: str,
    location: str = "",
    value: object = None,
) -> None:
    entry = {
        "severity": severity,  # "error" | "warning" | "info"
        "category": category,
        "message": message,
        "location": location,
    }
    if value is not None:
        entry["value"] = str(value)[:200]
    if severity == "error":
        issues.append(entry)
    else:
        warnings_list.append(entry)


# ---------------------------------------------------------------------------
# Schema validators
# ---------------------------------------------------------------------------

ISO_DATE_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}"  # date part
    r"(T\d{2}:\d{2}:\d{2}Z)?$"  # optional time part
)

FUNDING_RE = re.compile(
    r"""^(
        Undisclosed       |
        Bootstrapped.*    |
        Public.*          |
        Private.*         |
        \$[\d,.]+[MBK]?\+? |
        \$[\d,.]+\s*(million|billion)
    )""",
    re.VERBOSE | re.IGNORECASE,
)


def is_valid_iso_date(s: str) -> bool:
    return bool(ISO_DATE_RE.match(s))


def is_valid_url(s: str) -> bool:
    return isinstance(s, str) and s.startswith(("http://", "https://"))


def validate_vendors_json() -> list[dict]:
    """Validate data/vendors.json structure and content."""
    findings = []
    if not VENDORS_FILE.exists():
        add_issue("error", "schema", "vendors.json not found", str(VENDORS_FILE))
        return findings

    with VENDORS_FILE.open(encoding="utf-8") as f:
        data = json.load(f)

    # Required top-level keys
    for key in ("metadata", "categories"):
        if key not in data:
            add_issue("error", "schema", f"vendors.json missing required key: {key}", "root")

    meta = data.get("metadata", {})
    for mk in ("last_updated", "version", "total_vendors", "categories", "source"):
        if mk not in meta:
            add_issue("warning", "schema", f"metadata missing key: {mk}", "metadata")

    # Validate last_updated format
    lu = meta.get("last_updated", "")
    if lu and not is_valid_iso_date(lu):
        add_issue("error", "date_format", "metadata.last_updated is not ISO 8601", "metadata.last_updated", lu)

    categories = data.get("categories", {})
    if not isinstance(categories, dict) or len(categories) == 0:
        add_issue("error", "schema", "categories must be a non-empty object", "categories")
        return findings

    total_vendors = 0
    all_vendor_names = []
    all_source_urls = []

    required_vendor_keys = ("name", "website", "capabilities", "pricing_model", "status")

    for cat_key, category in categories.items():
        cat_path = f"categories.{cat_key}"

        if "description" not in category:
            add_issue("warning", "schema", "Category missing description", cat_path)

        vendors = category.get("vendors", [])
        if not isinstance(vendors, list) or len(vendors) == 0:
            add_issue("warning", "schema", "Category has no vendors", cat_path)
            continue

        for i, vendor in enumerate(vendors):
            vpath = f"{cat_path}.vendors[{i}]"
            total_vendors += 1
            name = vendor.get("name", f"[unnamed at index {i}]")
            all_vendor_names.append(name)

            # Required fields
            for field in required_vendor_keys:
                if field not in vendor:
                    add_issue("warning", "schema", f"Vendor '{name}' missing field: {field}", vpath)

            # Website must be valid URL
            website = vendor.get("website", "")
            if website and not is_valid_url(website):
                add_issue("error", "url_format", f"Vendor '{name}' has invalid website URL", f"{vpath}.website", website)

            # Status check
            status = vendor.get("status", "")
            if status not in ("Active", "Acquired", "Inactive", ""):
                add_issue("warning", "schema", f"Vendor '{name}' has unusual status", f"{vpath}.status", status)

            # Founded year sanity
            founded = vendor.get("founded")
            if founded is not None:
                if not isinstance(founded, int) or not (1960 <= founded <= 2030):
                    add_issue("warning", "data_range", f"Vendor '{name}' has unusual founded year", f"{vpath}.founded", founded)

            # Funding format
            funding = vendor.get("funding_total", "")
            if funding and not FUNDING_RE.match(str(funding)):
                add_issue("warning", "data_format", f"Vendor '{name}' has unusual funding_total format", f"{vpath}.funding_total", funding)

            # Collect source URLs for later link health check
            for url in vendor.get("source_urls", []):
                if is_valid_url(url):
                    all_source_urls.append({"vendor": name, "url": url})
                else:
                    add_issue("warning", "url_format", f"Vendor '{name}' has non-URL in source_urls", f"{vpath}.source_urls", url)

            # Capabilities must be a list
            caps = vendor.get("capabilities", [])
            if not isinstance(caps, list):
                add_issue("error", "schema", f"Vendor '{name}' capabilities must be a list", f"{vpath}.capabilities")

    # Check total_vendors metadata accuracy
    declared_count = meta.get("total_vendors", 0)
    if abs(declared_count - total_vendors) > 5:
        add_issue(
            "warning", "metadata",
            f"metadata.total_vendors ({declared_count}) differs significantly from actual count ({total_vendors})",
            "metadata.total_vendors",
        )

    # Check declared category count
    declared_cats = meta.get("categories", 0)
    actual_cats = len(categories)
    if isinstance(declared_cats, int) and declared_cats != actual_cats:
        add_issue(
            "warning", "metadata",
            f"metadata.categories ({declared_cats}) != actual categories ({actual_cats})",
            "metadata.categories",
        )

    # Duplicate vendor name check
    seen = set()
    for name in all_vendor_names:
        if name in seen:
            add_issue("warning", "duplicate", f"Duplicate vendor name: {name}", "categories")
        seen.add(name)

    findings.append({
        "file": "vendors.json",
        "total_vendors": total_vendors,
        "total_categories": actual_cats,
        "total_source_urls": len(all_source_urls),
    })
    return all_source_urls


def validate_market_data_json() -> list[dict]:
    """Validate data/market-data.json structure and content."""
    if not MARKET_DATA_FILE.exists():
        add_issue("error", "schema", "market-data.json not found", str(MARKET_DATA_FILE))
        return []

    with MARKET_DATA_FILE.open(encoding="utf-8") as f:
        data = json.load(f)

    for key in ("metadata", "market_size", "segments", "funding_rounds", "acquisitions"):
        if key not in data:
            add_issue("warning", "schema", f"market-data.json missing section: {key}", "root")

    # Validate estimates
    estimates = data.get("market_size", {}).get("estimates", [])
    if not estimates:
        add_issue("warning", "schema", "market_size.estimates is empty", "market_size.estimates")

    all_source_urls = []
    for i, est in enumerate(estimates):
        epath = f"market_size.estimates[{i}]"
        for field in ("analyst", "cagr", "unit"):
            if field not in est:
                add_issue("warning", "schema", f"Estimate missing field: {field}", epath)

        cagr = est.get("cagr")
        if cagr is not None:
            if not isinstance(cagr, (int, float)) or not (0 < cagr < 100):
                add_issue("warning", "data_range", f"Estimate CAGR value seems unrealistic", epath, cagr)

        # Validate market size values (billion USD range)
        for year_field in ("year_2024", "year_2025", "year_2030", "year_2035"):
            val = est.get(year_field)
            if val is not None:
                if not isinstance(val, (int, float)) or not (0.1 <= val <= 500):
                    add_issue("warning", "data_range", f"Market size {year_field} seems outside realistic range", epath, val)

        src = est.get("source_url", "")
        if src and is_valid_url(src):
            all_source_urls.append({"context": f"estimate[{i}]", "url": src})
        elif src:
            add_issue("warning", "url_format", "Non-URL in estimate source_url", epath, src)

    # Validate funding rounds
    for i, fr in enumerate(data.get("funding_rounds", [])):
        frpath = f"funding_rounds[{i}]"
        if "company" not in fr:
            add_issue("warning", "schema", "Funding round missing company", frpath)
        amount = fr.get("amount_usd_millions")
        if amount is not None and (not isinstance(amount, (int, float)) or amount <= 0 or amount > 100000):
            add_issue("warning", "data_range", "Funding amount outside realistic range", frpath, amount)
        date = fr.get("date", "")
        if date and not is_valid_iso_date(date):
            add_issue("error", "date_format", "Funding round date is not ISO 8601", f"{frpath}.date", date)
        src = fr.get("source_url", "")
        if src and is_valid_url(src):
            all_source_urls.append({"context": f"funding_round.{fr.get('company','?')}", "url": src})

    # Validate acquisitions
    for i, acq in enumerate(data.get("acquisitions", [])):
        apath = f"acquisitions[{i}]"
        for field in ("target", "acquirer", "date"):
            if field not in acq:
                add_issue("warning", "schema", f"Acquisition missing field: {field}", apath)
        date = acq.get("date", "")
        if date and not is_valid_iso_date(date):
            add_issue("error", "date_format", "Acquisition date is not ISO 8601", f"{apath}.date", date)
        src = acq.get("source_url", "")
        if src and is_valid_url(src):
            all_source_urls.append({"context": f"acquisition.{acq.get('target','?')}", "url": src})

    return all_source_urls


def validate_regulatory_json() -> list[dict]:
    """Validate data/regulatory-tracker.json structure and content."""
    if not REGULATORY_FILE.exists():
        add_issue("error", "schema", "regulatory-tracker.json not found", str(REGULATORY_FILE))
        return []

    with REGULATORY_FILE.open(encoding="utf-8") as f:
        data = json.load(f)

    for key in ("metadata", "regulations"):
        if key not in data:
            add_issue("error", "schema", f"regulatory-tracker.json missing key: {key}", "root")
            return []

    all_source_urls = []
    for i, reg in enumerate(data.get("regulations", [])):
        rpath = f"regulations[{i}]"
        name = reg.get("name", f"[unnamed at {i}]")

        for field in ("name", "jurisdiction", "status", "key_dates"):
            if field not in reg:
                add_issue("warning", "schema", f"Regulation '{name}' missing field: {field}", rpath)

        # Validate key_dates
        for j, kd in enumerate(reg.get("key_dates", [])):
            kdpath = f"{rpath}.key_dates[{j}]"
            if "date" not in kd:
                add_issue("warning", "schema", f"Regulation '{name}' key_date missing date", kdpath)
            date = kd.get("date", "")
            if date and not is_valid_iso_date(date):
                add_issue("error", "date_format", f"Regulation '{name}' key_date is not ISO 8601", f"{kdpath}.date", date)
            if "milestone" not in kd:
                add_issue("warning", "schema", f"Regulation '{name}' key_date missing milestone", kdpath)

        # Validate penalties if present
        penalties = reg.get("penalties")
        if penalties:
            for pfield in ("max_fine_euros", "max_revenue_percent", "prohibited_ai_max_fine_euros"):
                val = penalties.get(pfield)
                if val is not None and (not isinstance(val, (int, float)) or val <= 0):
                    add_issue("warning", "data_range", f"Regulation '{name}' penalty {pfield} unrealistic", f"{rpath}.penalties", val)

        src = reg.get("source_url", "")
        if src and is_valid_url(src):
            all_source_urls.append({"context": f"regulation.{name}", "url": src})
        elif src:
            add_issue("warning", "url_format", f"Regulation '{name}' source_url is not a valid URL", f"{rpath}.source_url", src)

    return all_source_urls


# ---------------------------------------------------------------------------
# URL health checker
# ---------------------------------------------------------------------------

def check_url_health(url_entries: list[dict], max_checks: int = MAX_URL_CHECKS) -> list[dict]:
    """Check a sample of URLs for liveness. Returns list of results."""
    results = []
    checked = 0
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
    }

    for entry in url_entries:
        if checked >= max_checks:
            logger.info("Reached MAX_URL_CHECKS (%d), stopping URL health check", max_checks)
            break

        url = entry.get("url", "")
        context = entry.get("context", entry.get("vendor", "?"))

        try:
            req = urllib.request.Request(url, headers=headers, method="HEAD")
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                status = resp.status
        except urllib.error.HTTPError as e:
            status = e.code
        except Exception as e:
            status = -1
            logger.debug("URL check failed for %s: %s", url, e)

        live = 200 <= status < 400
        result = {
            "url": url,
            "context": context,
            "status": status,
            "live": live,
        }
        results.append(result)

        if not live:
            add_issue(
                "warning",
                "url_health",
                f"URL returned non-2xx/3xx status ({status}): {url}",
                context,
                url,
            )

        checked += 1
        time.sleep(0.3)  # Polite delay

    live_count = sum(1 for r in results if r["live"])
    logger.info(
        "URL health check: %d/%d live (%d skipped)",
        live_count, len(results), max(0, len(url_entries) - len(results))
    )
    return results


# ---------------------------------------------------------------------------
# Anomaly detection
# ---------------------------------------------------------------------------

def detect_anomalies(vendors_data: dict, market_data: dict) -> None:
    """Detect statistical and logical anomalies in the datasets."""
    categories = vendors_data.get("categories", {})

    # Check for categories with very few vendors
    for cat_key, cat in categories.items():
        vendors = cat.get("vendors", [])
        if len(vendors) == 0:
            add_issue("error", "anomaly", f"Category '{cat_key}' has zero vendors", f"categories.{cat_key}")
        elif len(vendors) == 1:
            add_issue("info", "anomaly", f"Category '{cat_key}' has only 1 vendor", f"categories.{cat_key}")

    # Check for vendors with no capabilities listed
    for cat_key, cat in categories.items():
        for vendor in cat.get("vendors", []):
            caps = vendor.get("capabilities", [])
            if isinstance(caps, list) and len(caps) == 0:
                add_issue(
                    "warning", "anomaly",
                    f"Vendor '{vendor.get('name')}' has empty capabilities list",
                    f"categories.{cat_key}",
                )

    # Market data: check that growth projections are consistent
    estimates = market_data.get("market_size", {}).get("estimates", [])
    for est in estimates:
        y2024 = est.get("year_2024")
        y2025 = est.get("year_2025")
        if y2024 and y2025 and y2025 < y2024:
            add_issue(
                "error", "anomaly",
                f"Market estimate from '{est.get('analyst')}': year_2025 < year_2024 (shrinking market?)",
                "market_size.estimates",
                f"{y2024} -> {y2025}",
            )

    # Check acquisitions have at least acquirer + target
    for acq in market_data.get("acquisitions", []):
        if not acq.get("acquirer") or not acq.get("target"):
            add_issue("warning", "anomaly", "Acquisition record missing acquirer or target", "acquisitions")


# ---------------------------------------------------------------------------
# GitHub Issues integration (CI mode)
# ---------------------------------------------------------------------------

def create_github_issue(title: str, body: str) -> bool:
    """Create a GitHub issue when running in CI with GITHUB_TOKEN."""
    token = os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not token or not repo:
        logger.debug("Skipping GitHub issue creation (no GITHUB_TOKEN or GITHUB_REPOSITORY)")
        return False

    api_url = f"https://api.github.com/repos/{repo}/issues"
    payload = json.dumps({
        "title": title,
        "body": body,
        "labels": GITHUB_ISSUE_LABELS,
    }).encode("utf-8")

    req = urllib.request.Request(
        api_url,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status in (200, 201):
                body_resp = json.loads(resp.read().decode("utf-8"))
                logger.info("Created GitHub issue: %s", body_resp.get("html_url"))
                return True
    except Exception as e:  # noqa: BLE001
        logger.warning("Failed to create GitHub issue: %s", e)
    return False


def maybe_create_github_issues(error_issues: list[dict]) -> None:
    """Create one consolidated GitHub issue for all errors in CI."""
    if not error_issues:
        return

    lines = ["## AI TRiSM Index \u2014 Data Validation Errors\n"]
    lines.append(f"Detected {len(error_issues)} error(s) during automated validation.\n")
    lines.append("| Severity | Category | Location | Message |")
    lines.append("|----------|----------|----------|---------|")
    for issue in error_issues:
        lines.append(
            f"| {issue['severity']} | {issue['category']} | {issue.get('location','')} | {issue['message']} |"
        )
    lines.append(f"\n_Generated at {datetime.now(timezone.utc).isoformat()} by validate_data.py_")

    create_github_issue(
        title=f"[Automated] Data validation: {len(error_issues)} error(s) detected",
        body="\n".join(lines),
    )


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(
    schema_findings: list[dict],
    url_results: list[dict],
    run_args: argparse.Namespace,
) -> dict:
    error_count = len(issues)
    warning_count = len(warnings_list)

    live_urls = sum(1 for r in url_results if r.get("live"))
    dead_urls = sum(1 for r in url_results if not r.get("live"))

    report = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "overall_status": "PASS" if error_count == 0 else "FAIL",
        "summary": {
            "errors": error_count,
            "warnings": warning_count,
            "urls_checked": len(url_results),
            "urls_live": live_urls,
            "urls_dead": dead_urls,
        },
        "schema_findings": schema_findings,
        "errors": issues,
        "warnings": warnings_list,
        "url_health": url_results,
    }
    return report


# ---------------------------------------------------------------------------
# CLI argument parsing
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate AI TRiSM Market Index data files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--ci",
        action="store_true",
        help="CI mode: exit non-zero on any errors; create GitHub Issues on failure",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output validation report as JSON to stdout",
    )
    parser.add_argument(
        "--check",
        choices=["all", "schema", "urls", "anomalies"],
        default="all",
        help="Which checks to run (default: all)",
    )
    parser.add_argument(
        "--max-url-checks",
        type=int,
        default=MAX_URL_CHECKS,
        help=f"Maximum number of URLs to check (default: {MAX_URL_CHECKS})",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    args = parse_args()
    logger.info("=== AI TRiSM Market Index \u2014 validate_data.py ===")
    logger.info("Check mode: %s", args.check)

    schema_findings = []
    all_urls = []

    # Load data files for anomaly detection
    vendors_data: dict = {}
    market_data: dict = {}

    if args.check in ("all", "schema"):
        logger.info("--- Schema validation ---")

        vendor_urls = validate_vendors_json()
        all_urls.extend(vendor_urls)
        schema_findings.append({"file": "vendors.json", "source_urls_found": len(vendor_urls)})

        market_urls = validate_market_data_json()
        all_urls.extend(market_urls)
        schema_findings.append({"file": "market-data.json", "source_urls_found": len(market_urls)})

        reg_urls = validate_regulatory_json()
        all_urls.extend(reg_urls)
        schema_findings.append({"file": "regulatory-tracker.json", "source_urls_found": len(reg_urls)})

        logger.info(
            "Schema checks complete. Errors: %d, Warnings: %d, URLs collected: %d",
            len(issues), len(warnings_list), len(all_urls)
        )

        # Load for anomaly detection
        if VENDORS_FILE.exists():
            with VENDORS_FILE.open(encoding="utf-8") as f:
                vendors_data = json.load(f)
        if MARKET_DATA_FILE.exists():
            with MARKET_DATA_FILE.open(encoding="utf-8") as f:
                market_data = json.load(f)

    if args.check in ("all", "anomalies") and vendors_data and market_data:
        logger.info("--- Anomaly detection ---")
        detect_anomalies(vendors_data, market_data)
        logger.info(
            "Anomaly checks complete. Errors: %d, Warnings: %d",
            len(issues), len(warnings_list)
        )

    url_results = []
    if args.check in ("all", "urls"):
        logger.info("--- URL health checks (%d URLs, max %d) ---", len(all_urls), args.max_url_checks)
        url_results = check_url_health(all_urls, max_checks=args.max_url_checks)

    # Generate and save report
    report = generate_report(schema_findings, url_results, args)
    VALIDATION_REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with VALIDATION_REPORT_FILE.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    logger.info("Validation report saved to %s", VALIDATION_REPORT_FILE)

    # Output
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        _print_human_report(report)

    # CI mode
    if args.ci and issues:
        maybe_create_github_issues(issues)
        logger.error("CI mode: %d error(s) detected. Exiting with code 1.", len(issues))
        return 1

    return 0


def _print_human_report(report: dict) -> None:
    """Print a human-readable summary to stdout."""
    status = report["overall_status"]
    summary = report["summary"]

    sep = "=" * 60
    print(f"\n{sep}")
    print(f"  AI TRiSM Market Index \u2014 Validation Report")
    print(f"  Status: {status}")
    print(f"{sep}")
    print(f"  Errors:           {summary['errors']}")
    print(f"  Warnings:         {summary['warnings']}")
    print(f"  URLs checked:     {summary['urls_checked']}")
    print(f"  URLs live:        {summary['urls_live']}")
    print(f"  URLs unreachable: {summary['urls_dead']}")
    print(f"{sep}\n")

    if report["errors"]:
        print("ERRORS:")
        for issue in report["errors"]:
            loc = f" [{issue.get('location','')}]" if issue.get("location") else ""
            print(f"  \u2717 [{issue['category']}]{loc} {issue['message']}")

    if report["warnings"]:
        print("\nWARNINGS:")
        for warn in report["warnings"][:20]:  # Cap display to 20
            loc = f" [{warn.get('location','')}]" if warn.get("location") else ""
            print(f"  \u26a0 [{warn['category']}]{loc} {warn['message']}")
        if len(report["warnings"]) > 20:
            print(f"  ... and {len(report['warnings']) - 20} more (see validation-report.json)")

    print(f"\nFull report: {VALIDATION_REPORT_FILE}\n")


if __name__ == "__main__":
    sys.exit(main())

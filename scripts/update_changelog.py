#!/usr/bin/env python3
"""Auto-update CHANGELOG.md with data refresh entries."""
import json
import datetime
import os
import sys

def main():
    today = datetime.date.today().isoformat()
    changelog_path = "CHANGELOG.md"
    report_path = "data/fetch-report.json"
    vendors_path = "data/vendors.json"

    # Get vendor count
    vendor_count = "?"
    try:
        with open(vendors_path) as f:
            d = json.load(f)
        vendor_count = sum(len(c.get("vendors", [])) for c in d.get("categories", {}).values())
    except Exception:
        pass

    # Get fetch report stats
    live = "?"
    unreachable = "?"
    try:
        with open(report_path) as f:
            r = json.load(f)
        s = r.get("summary", {})
        live = s.get("websites_live", "?")
        unreachable = s.get("websites_unreachable", "?")
    except Exception:
        pass

    # Build the new entry
    entry = f"\n### Auto-Refresh -- {today}\n\n"
    entry += f"- Vendor websites checked: {vendor_count} total, {live} live, {unreachable} unreachable\n"
    entry += f"- Data files refreshed via automated pipeline\n"

    # Read existing changelog
    with open(changelog_path, "r") as f:
        content = f.read()

    # Check if today's entry already exists
    if f"Auto-Refresh -- {today}" in content:
        print(f"CHANGELOG already has entry for {today}, skipping")
        return

    # Insert after the first --- separator (after the version header block)
    # Find "## 1.0.0" or first "---"
    idx = content.find("## 1.0.0")
    if idx == -1:
        idx = content.find("---")
    if idx != -1:
        hr_idx = content.find("---", idx)
        if hr_idx != -1:
            insert_pos = hr_idx + 3
            content = content[:insert_pos] + "\n" + entry + content[insert_pos:]

    with open(changelog_path, "w") as f:
        f.write(content)

    print(f"CHANGELOG.md updated with auto-refresh entry for {today}")

if __name__ == "__main__":
    main()

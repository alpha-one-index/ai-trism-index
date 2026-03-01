# Data Methodology

> Standards, verification processes, update schedules, and staleness policies for all data in the AI TRiSM Market Index.

---

## Overview

The AI TRiSM Market Index follows the same four-tier data verification framework as the [ai-infra-index](https://github.com/alpha-one-index/ai-infra-index). Every data point in this repository is sourced, verified, and maintained according to the standards below. No data is included without a traceable primary or secondary source.

This methodology document is the reference for:
- How data is collected and verified
- How often data is updated
- What happens when data becomes stale
- How errors are corrected
- How to interpret data quality levels

---

## Table of Contents

1. [Four-Tier Verification Framework](#four-tier-verification-framework)
2. [Update Schedule](#update-schedule)
3. [Staleness Policy](#staleness-policy)
4. [Data Quality Levels](#data-quality-levels)
5. [Error Handling and Correction](#error-handling-and-correction)
6. [Source Hierarchy](#source-hierarchy)
7. [Known Limitations](#known-limitations)
8. [Versioning Policy](#versioning-policy)

---

## Four-Tier Verification Framework

All data in this repository is assigned to one of four verification tiers based on source type and verification method.

---

### Tier 1: Vendor Source Verification

**Definition:** Data sourced directly from the company, organization, or entity the data describes.

**Accepted sources:**
- Official company websites (About, Press, Investor Relations pages)
- Official press releases (sourced from company newsroom or PR distribution services: PR Newswire, Business Wire, GlobeNewswire)
- Official product documentation and technical documentation
- Official job postings (for HQ, team size, technology stack inference)
- Official social media announcements from verified corporate accounts

**Verification process:**
1. Primary source URL recorded at time of data collection
2. Source publication date recorded
3. Data recency confirmed (not older than 12 months for funding data; not older than 6 months for capability claims)

**Tier 1 examples in this repository:**
- Credo AI $21M funding: [Business Wire (July 2024)](https://www.businesswire.com/news/home/20240730411517/en/Credo-AI-Announces-$21-Million-in-New-Capital)
- Arize AI $70M Series C: [PR Newswire (February 2025)](https://www.prnewswire.com/news-releases/arize-ai-secures-70m-series-c-to-fix-ais-biggest-problem-making-llms-and-ai-agents-work-in-the-real-world-302381601.html)
- Veeam acquires Securiti AI: [Veeam press release (December 2025)](https://www.veeam.com/company/press-release/veeam-acquires-securiti-ai.html)
- EU AI Act full text: [EUR-Lex (EU Official Journal)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)

**Tier 1 limitations:**
- Companies may not disclose accurate figures (puffery in press releases)
- Announced funding may differ from actual investment amounts
- Capability claims from vendors must be cross-referenced with Tier 2 (analyst verification)

---

### Tier 2: Analyst Cross-Reference

**Definition:** Data cross-referenced against independent analyst research from recognized industry research firms.

**Accepted sources:**
- Gartner Market Guides, Magic Quadrants, Hype Cycles, Cool Vendor reports
- Forrester Wave reports, Tech Radar reports
- IDC MarketScape reports, IDC research
- MarketsandMarkets reports
- Precedence Research reports
- Research and Markets reports
- Allied Market Research reports
- Polaris Market Research reports
- CB Insights reports and rankings

**Verification process:**
1. Analyst firm and report title recorded
2. Publication date recorded
3. Specific citation (page, section, or excerpt) noted where available
4. For market size data: consensus across multiple analysts reported; individual estimates not treated as definitive

**Tier 2 examples in this repository:**
- Market size $2.95B (2025): [Precedence Research](https://www.precedenceresearch.com/ai-trust-risk-and-security-management-market)
- AI Governance market $0.89B at 45.3% CAGR: [MarketsandMarkets AI Governance](https://www.marketsandmarkets.com/Market-Reports/ai-governance-market-176187291.html)
- Gartner Representative Vendors (2025): via vendor press releases citing the Gartner Market Guide for AI TRiSM (February 18, 2025)
- Gartner Cool Vendors in Agentic AI TRiSM (September 2, 2025): [Business Wire citing Gartner](https://www.businesswire.com/news/home/20250910440978/en/Zenity-Named-a-2025-Gartner-Cool-Vendor-in-Agentic-AI-Trust-Risk-and-Security-Management-Report)

**Tier 2 limitations:**
- Full Gartner, Forrester, and IDC reports are behind paywalls — this repository references publicly available summaries, vendor press releases citing these reports, and excerpts released publicly by the analysts
- Analyst estimates reflect point-in-time views; markets evolve between report cycles
- Different analysts use different scope definitions (especially for market sizing)

---

### Tier 3: Regulatory Source Verification

**Definition:** Regulatory data sourced directly from official government, standards body, or regulatory authority publications.

**Accepted sources:**
- EU Official Journal and EUR-Lex (EU legislation)
- Artificialintelligenceact.eu (EU AI Act article-level reference)
- NIST AI Resource Center (airc.nist.gov)
- ISO official standards database (iso.org)
- US Federal Register
- White House official publications (whitehouse.gov)
- NCSL (National Conference of State Legislatures) AI legislation tracker
- Federal Reserve (federalreserve.gov) — SR 11-7
- Bank of England (bankofengland.co.uk) — SS1/23
- FDA (fda.gov) — medical device AI guidance
- HHS/OCR (hhs.gov) — HIPAA guidance
- China CAC official publications (cac.gov.cn)

**Verification process:**
1. Official text URL recorded (not secondary commentary)
2. Date of entry into force or publication recorded
3. Article/section cited for specific provisions
4. Recent amendments or updates tracked

**Tier 3 examples in this repository:**
- EU AI Act Article 5 prohibited AI: [artificialintelligenceact.eu/article/5/](https://artificialintelligenceact.eu/article/5/)
- NIST AI RMF 1.0: [airc.nist.gov](https://airc.nist.gov/Home)
- ISO/IEC 42001: [iso.org/standard/81230.html](https://www.iso.org/standard/81230.html)
- Federal Reserve SR 11-7: [federalreserve.gov/supervisionreg/srletters/sr1107.htm](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm)
- China GenAI Measures: [cac.gov.cn](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)

**Tier 3 limitations:**
- Regulatory guidance is subject to change; this repository tracks the most recent version but may lag by up to 14 days for new developments
- Legal interpretation of regulations varies; this repository describes provisions but does not constitute legal advice
- China regulatory sources are in Chinese; this repository uses authoritative translations from recognized legal firms

---

### Tier 4: Funding Verification

**Definition:** Funding amounts and M&A deal prices verified against multiple independent financial reporting sources.

**Accepted sources:**
- SEC filings (EDGAR) for public companies
- Official press releases on PR Newswire, Business Wire, GlobeNewswire (Tier 1 sub-source)
- TechCrunch venture capital reporting
- VentureBeat venture capital reporting
- SecurityWeek cybersecurity M&A reporting
- CyberScoop cybersecurity M&A reporting
- Crunchbase (for cross-reference; not sole source)
- Bloomberg / Reuters / Wall Street Journal (for major transactions)
- LinkedIn announcements from company executives (supporting source only)

**Verification process:**
1. Minimum two independent sources for any funding amount
2. Date of funding announcement recorded
3. Investor names verified against press release
4. M&A deal prices: primary source is acquirer or target press release; confirmed by financial press coverage

**Tier 4 examples in this repository:**
- Veeam acquires Securiti for $1.725B: [Veeam press release](https://www.veeam.com/company/press-release/veeam-acquires-securiti-ai.html) + [TechCrunch](https://techcrunch.com/2025/10/21/veeam-acquires-data-security-company-securiti-ai-for-1-7b/)
- F5 acquires CalypsoAI for $180M: [CyberScoop](https://cyberscoop.com/f5-to-acquire-ai-security-firm-calypsoai-for-180-million/) + [SecurityWeek](https://www.securityweek.com/f5-to-acquire-calypsoai-for-180-million/)
- HiddenLayer Series A $50M: [PR Newswire](https://www.prnewswire.com/news-releases/hiddenlayer-raises-50m-in-series-a-funding-to-safeguard-ai-301931260.html)

**Tier 4 limitations:**
- Many M&A deal prices are "undisclosed" — implied values are noted explicitly as estimates, not confirmed figures
- Seed round and pre-seed funding is often not publicly announced; "undisclosed" in vendor profiles means not publicly confirmed
- Crunchbase and similar databases may lag actual funding announcements by weeks or months

---

## Update Schedule

| Data Category | Update Frequency | Trigger |
|--------------|-----------------|---------|
| **Vendor funding and status** | Weekly | New press releases; vendor announcements; M&A news |
| **M&A activity** | As deals are announced | Any AI TRiSM acquisition or merger |
| **Market sizing data** | Monthly | New analyst report publication |
| **Regulatory data (EU AI Act, NIST, ISO)** | As regulations change | New text, amendments, or implementation guidance |
| **US state AI laws** | Monthly | NCSL tracker and state legislative updates |
| **Gartner framework** | Per Gartner publication | New Market Guide, Magic Quadrant, or Hype Cycle publication |
| **Vendor capabilities** | Monthly | Product updates, press releases, new feature announcements |
| **Platform comparison matrices** | Monthly | Verified changes to vendor capabilities or pricing |
| **Implementation guide** | Quarterly | New best practices, regulatory guidance, or community feedback |

---

## Staleness Policy

Data is considered **stale** when it exceeds the following age thresholds without re-verification:

| Data Type | Stale After | Action Required |
|-----------|------------|-----------------|
| Vendor funding (total raised) | 90 days | Re-verify against latest press releases and Crunchbase |
| Vendor status (acquired/independent) | 30 days | Re-verify against official announcements |
| Market sizing (forecast) | 12 months | Flag for analyst report update check |
| Regulatory effective dates | Upon change | Update within 14 days of effective date |
| Vendor capabilities | 90 days | Re-verify against vendor product documentation |
| Pricing information | 60 days | Re-verify against vendor pricing pages / sales confirmation |
| Gartner recognitions | Per Gartner cycle (~12–18 months) | Re-verify when new Market Guide published |

**Stale data handling:**
1. Data older than the stale threshold is flagged with `> ⚠️ Data may be outdated — last verified [date]` in the source file
2. Stale data is prioritized for re-verification in the next weekly update cycle
3. If stale data cannot be re-verified within 30 days of flagging, it is either updated with latest information or removed

---

## Data Quality Levels

| Level | Symbol | Meaning |
|-------|--------|---------|
| **Verified** | ✅ | Tier 1 or Tier 3 primary source + Tier 2 or Tier 4 cross-reference |
| **Sourced** | 🔗 | Single Tier 1 or Tier 3 source; not cross-referenced |
| **Analyst-cited** | 📊 | Tier 2 analyst reference only; not independently verified |
| **Estimated** | ~  | Implied value (e.g., acquisition price implied by deal context); explicitly noted as estimate |
| **Undisclosed** | — | No public data available; company/parties have not disclosed |

---

## Error Handling and Correction

### Reporting Errors

To report a data error:
1. Open a GitHub Issue with the label `data-error`
2. Include: the incorrect data point, the file and section, the correct value, and a source URL
3. Errors are reviewed within 72 hours

### Correction Process

1. Issue opened with `data-error` label
2. Maintainer reviews the claim and verifies the correction against Tier 1–4 sources
3. If verified: correction applied in the relevant spec file; commit note references the issue
4. CHANGELOG.md updated with correction note
5. Issue closed with reference to correcting commit

### Retroactive corrections

If a correction changes historical data (e.g., a funding amount was previously misreported), the corrected version replaces the old version with a note: `*(Corrected from [old value] on [date] — see issue #X)*`

---

## Source Hierarchy

When sources conflict, the following hierarchy applies:

1. **Official regulatory text** (EU Official Journal, ISO, NIST official publications) — highest authority for regulatory data
2. **SEC filings** — highest authority for publicly traded company financial data
3. **Official press releases** (from company or acquirer) — highest authority for funding and M&A data
4. **Named analyst reports** (Gartner, Forrester, IDC, MarketsandMarkets) — highest authority for market sizing and vendor recognition
5. **Reputable financial/tech press** (TechCrunch, Bloomberg, Reuters, SecurityWeek) — for cross-reference and corroboration
6. **Vendor marketing claims** — must be cross-referenced against Tier 2 before inclusion

---

## Known Limitations

1. **Analyst report paywalls:** Gartner, Forrester, and IDC reports are behind paywalls. This repository references these reports via vendor press releases, analyst social media, and publicly available summaries — not the full reports. Exact wording from reports may not be reproduced verbatim.

2. **Undisclosed funding:** Many AI TRiSM startups have not publicly disclosed funding amounts. "Undisclosed" means not publicly confirmed — not that no funding exists.

3. **Market sizing variance:** AI TRiSM market size estimates vary significantly across analyst firms ($1.7B–$3.5B in 2025) due to differing scope definitions. The README and market-sizing.md present multiple estimates and explain the variance. No single estimate should be cited as "the" market size.

4. **M&A price undisclosed:** Several AI TRiSM acquisitions have undisclosed prices. Implied values (noted as estimates with ~) are based on funding raised and comparable transaction multiples — not confirmed figures.

5. **Regulatory interpretation:** This repository describes AI regulations as written. Legal interpretation varies by jurisdiction and context. Nothing in this repository constitutes legal advice. Consult qualified legal counsel for compliance determinations.

6. **Vendor capability claims:** Vendor capability descriptions are based on vendor-published information and available analyst assessments. Independent testing of all capabilities claimed has not been performed by Alpha One Index.

7. **Timing lag:** There is an unavoidable lag between real-world events (funding announcements, acquisitions, regulatory updates) and this repository's updates. The weekly vendor data update cycle means events may be reflected with up to a 7-day delay.

---

## Versioning Policy

This repository follows [Semantic Versioning](https://semver.org/):

- **Major version (x.0.0):** Structural changes to the repository format; fundamental changes to data scope or methodology
- **Minor version (1.x.0):** New files, new categories, new vendor profiles added
- **Patch version (1.0.x):** Data updates, corrections, vendor profile updates, regulatory updates

Version 1.0.0 represents the initial public release with complete coverage of all sections.

See [CHANGELOG.md](CHANGELOG.md) for complete version history.

---

*This methodology was established for Version 1.0.0 of the AI TRiSM Market Index (March 2026). Any changes to the methodology are documented in CHANGELOG.md and take effect with the next minor or major release.*

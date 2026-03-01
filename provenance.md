# Data Provenance Card — AI TRiSM Market Index

**Version:** 1.0.0  
**Last Updated:** 2026-03-01  
**Maintained by:** [Alpha One Index](https://github.com/alpha-one-index)  
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
**Repository:** https://github.com/alpha-one-index/ai-trism-index

---

## Overview

The AI TRiSM Market Index is an open, machine-readable dataset covering the global market for AI Trust, Risk, and Security Management (AI TRiSM). This provenance card documents the sources, methodology, quality controls, and known limitations of the dataset.

---

## Dataset Files

| File | Description | Rows / Records |
|------|-------------|----------------|
| `data/vendors.json` | AI TRiSM vendor database | 66+ vendors across 10 categories |
| `data/market-data.json` | Market sizing, segments, M&A | 8 analyst estimates, 13 funding rounds, 8 acquisitions |
| `data/regulatory-tracker.json` | Global AI regulatory tracker | 10 regulations + 3 voluntary frameworks |
| `data/validation-report.json` | Automated quality report | Auto-generated |
| `data/history/vendors-YYYY-MM-DD.json` | Daily history snapshots | Auto-archived |

---

## Primary Data Sources

### Analyst Reports (Market Data)

| Source | Report | URL |
|--------|--------|-----|
| Precedence Research | AI TRiSM Market Global Forecast to 2035 | https://www.precedenceresearch.com/ai-trust-risk-and-security-management-market |
| MarketsandMarkets | AI Governance Market — Global Forecast to 2029 | https://www.marketsandmarkets.com/Market-Reports/ai-governance-market-176187291.html |
| Research and Markets | AI TRiSM Trends 2025-2030 | https://www.globenewswire.com/news-release/2025/05/21/3085951/28124/en/AI-Trust-Risk-and-Security-Management-Trends-Analysis-and-Growth-Forecasts-2025-2030-Market-to-Reach-7-44-Billion-Generative-AI-Foundation-Models-Spur-Demand-for-Advanced-AI-TRiSM-.html |
| Polaris Market Research | AI TRiSM Market | https://www.polarismarketresearch.com/industry-analysis/ai-trust-risk-and-security-management-market |
| Allied Market Research | AI TRiSM Market | https://www.alliedmarketresearch.com/press-release/ai-trust-risk-and-security-management-ai-trism-market.html |
| Market.us | AI TRiSM Market (Feb 2024) | https://market.us/report/ai-trust-risk-and-security-management-ai-trism-market/ |
| Yahoo Finance / Business Research | AI TRiSM Forecast (Jan 2026) | https://finance.yahoo.com/news/11-81-bn-ai-trust-121300066.html |
| AWS Marketplace | AI Governance Market | https://aws.amazon.com/marketplace/pp/prodview-vqc2rbyqo4gbc |

### Gartner Research (via Vendor Citations)

Gartner reports are proprietary. Gartner data in this index is sourced from:
- Vendor press releases citing Gartner recognition (linked in `source_urls` fields)
- Vendor blog posts announcing Gartner recognition
- LinkedIn posts from Gartner analysts (e.g., Avivah Litan)

Gartner reports referenced:
- **2025 Market Guide for AI TRiSM** — https://www.gartner.com/en/documents/5636393
- **Cool Vendors in AI Cybersecurity Governance 2025**
- **Cool Vendors in Agentic AI TRiSM 2025** — https://www.linkedin.com/posts/avivahlitan_ai-guardian-agents-activity-7369109299882635265-xqMi
- **Gartner Hype Cycle for AI 2025** — https://resilienceforward.com/gartner-expects-ai-trust-risk-and-security-management-trism-to-reach-mainstream-adoption-within-the-next-5-years/

### Regulatory Sources

| Regulation | Source |
|-----------|--------|
| EU AI Act | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 |
| NIST AI RMF 1.0 | https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf |
| ISO/IEC 42001:2023 | https://www.iso.org/standard/81230.html |
| SR 11-7 | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm |
| GDPR Article 22 | https://gdpr-info.eu/art-22-gdpr/ |

---

## Data Collection Methodology

1. **Inclusion criteria:** A vendor must have (a) a publicly announced AI TRiSM product or service, (b) verifiable company existence, and (c) at least one cited source URL.
2. **Funding data:** Sourced from official press releases and reputable financial media. Only announced rounds included.
3. **Gartner recognition:** Only noted when the vendor has publicly announced the recognition via official press release or blog post.
4. **Acquisition status:** Sourced from acquisition announcements. Acquired vendors retain their profile with `"status": "Acquired"`.

---

## Automated Updates

The dataset is updated via GitHub Actions:

1. **fetch_vendors.py** runs hourly via `.github/workflows/update-data.yml`
2. **validate_data.py** runs on every push via `.github/workflows/validate.yml`

---

## Known Limitations

1. **Incomplete private funding:** Only disclosed rounds are counted.
2. **Analyst scope divergence:** Market size estimates vary 2–5x across analysts due to different scope definitions.
3. **Acquisition lag:** Acquired vendors are updated when public announcements are made.
4. **Capability staleness:** Vendor capabilities may lag behind product updates.
5. **Geographic bias:** Coverage may be biased toward US and European vendors.
6. **Not investment advice:** This dataset is for market research and vendor evaluation only.

---

## Citation

```
Alpha One Index (2026). AI TRiSM Market Index (Version 1.0.0).
https://github.com/alpha-one-index/ai-trism-index
License: CC BY 4.0
```

---

## Contact

**Email:** alpha.one.hq@proton.me  
**GitHub Issues:** https://github.com/alpha-one-index/ai-trism-index/issues

---

*Last updated: 2026-03-01 | Generated by Alpha One Index*

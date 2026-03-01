# Contributing to the AI TRiSM Market Index

Thank you for considering a contribution to the AI TRiSM Market Index. This repository aims to be the most accurate, well-sourced, and comprehensive open reference for the AI Trust, Risk, and Security Management market. Every contribution is welcome — from fixing a typo to adding a new vendor profile.

---

## Table of Contents

- [What Kinds of Contributions Are Welcome?](#what-kinds-of-contributions-are-welcome)
- [How to Submit a Contribution](#how-to-submit-a-contribution)
- [Data Quality Standards](#data-quality-standards)
- [Contribution Templates](#contribution-templates)
- [Review Process](#review-process)
- [Code of Conduct](#code-of-conduct)
- [Contact](#contact)

---

## What Kinds of Contributions Are Welcome?

### High-Priority Contributions

| Contribution Type | Examples |
|-----------------|---------|
| **Funding updates** | New venture rounds, M&A deal prices, changes to vendor status |
| **New vendor profiles** | AI TRiSM vendors not yet in the index |
| **Regulatory updates** | New regulations, amendments, effective date updates |
| **Market sizing** | New analyst reports with AI TRiSM market size estimates |
| **Gartner/analyst recognition** | New Gartner Market Guide, Cool Vendor, or Hype Cycle mentions |
| **Error corrections** | Incorrect data with correct sourced value |

### Welcome Contributions

| Contribution Type | Examples |
|-----------------|---------|
| **Capability updates** | Vendor feature additions, product name changes, pricing changes |
| **New spec sections** | Well-sourced sections covering topics not yet covered |
| **Source improvements** | Better primary sources for existing data points |
| **Typos and grammar** | Always welcome |
| **Translation** | Non-English language regulatory sources with translations |

### Not Accepted

| Type | Reason |
|------|--------|
| Unsourced claims | Every data point must have a source URL |
| Vendor self-promotion without citations | Press releases OK; marketing copy without specifics is not |
| Legal advice | This repository describes regulations; it does not interpret them for specific situations |
| Speculation or predictions without analyst citation | Market predictions must cite a named analyst source |
| Pricing data without verification | Vendor pricing must be verified against official pricing pages or press announcements |

---

## How to Submit a Contribution

### Option 1: GitHub Issue (preferred for data errors and simple updates)

1. Go to the [Issues tab](https://github.com/alpha-one-index/ai-trism-index/issues)
2. Click **New Issue**
3. Select the appropriate template:
   - `data-error` — for corrections to existing data
   - `new-vendor` — for new vendor profile additions
   - `regulatory-update` — for regulatory changes
   - `market-data` — for new market sizing or analyst data
   - `general` — for all other contributions
4. Fill in the template completely, including source URLs
5. Submit the issue

### Option 2: Pull Request (for substantive additions)

1. Fork the repository
2. Create a branch: `git checkout -b update/[vendor-name]` or `git checkout -b add/[vendor-name]`
3. Make your changes following the [Data Quality Standards](#data-quality-standards) below
4. Ensure all new data has source URLs
5. Update the relevant spec file
6. Submit a Pull Request with:
   - Clear description of what changed
   - Reason for the change
   - Source URLs for all new data
   - Reference to the related issue (if applicable)

---

## Data Quality Standards

All contributions must meet the standards defined in [METHODOLOGY.md](METHODOLOGY.md). Key requirements:

### Required for Every Data Point

1. **Source URL** — Every factual claim must include a linked source in Markdown format: `[Source Name](URL)`
2. **Publication date** — For funding, M&A, and analyst data, include the publication date in the source citation: `[TechCrunch (March 2024)](https://...)`
3. **Source tier** — Prefer primary sources (Tier 1: company press releases, official documents) over secondary sources (Tier 2: analyst reports, tech press)

### Vendor Profile Format

New vendor profiles must include at minimum:

```markdown
### [Vendor Name]

- **Website:** https://[vendor-website]
- **Founded:** [Year]
- **HQ:** [City, State/Country]
- **Total Funding:** [Amount or "Undisclosed"]
- **Key Capabilities:** [3-5 bullet points]
- **Pricing Model:** [Enterprise SaaS / Usage-based / Open source / etc.]
- **Differentiator:** [What makes this vendor distinct]
- **Sources:** [Source 1](URL), [Source 2](URL)
```

If funding is undisclosed, note it as `Undisclosed` — do not omit.

### Market Data Format

New market sizing data must include:

```markdown
| [Analyst Firm] | [2024/2025 Value] | [Forecast Value] by [Year] | [CAGR]% | [Source](URL) |
```

### Regulatory Data Format

New regulatory entries must include:
- Regulation full name and short name
- Jurisdiction and enforcing authority
- Effective date
- Key AI-relevant provisions
- Official source URL (primary legislative text, not commentary)

---

## Contribution Templates

### New Vendor Profile Template

```markdown
### [Vendor Name]

- **Website:** https://[url]
- **Founded:** [Year]
- **HQ:** [City, State/Country]
- **Total Funding:** $[Amount]M ([Round type] [Month Year]; lead investor: [Name]; co-investors: [Names])
- **Key Capabilities:**
  - [Capability 1]
  - [Capability 2]
  - [Capability 3]
- **Notable Customers/Partners:** [Names if publicly available]
- **Pricing Model:** [Enterprise SaaS / Usage-based / Open source + enterprise / etc.]
- **Gartner AI TRiSM Layer:** [Layer 1: AI Governance / Layer 2: Runtime / Layer 3: Info Governance / Layer 4: Infra]
- **Differentiator:** [What makes this vendor distinct from competitors]
- **Sources:** [Source Name (Month Year)](URL), [Source Name (Month Year)](URL)
```

---

### Funding Update Template

```markdown
**[Vendor Name] — Funding Update**

- **Round:** [Series A / B / C / Seed / Growth / Undisclosed]
- **Amount:** $[X]M
- **Date:** [Month Year]
- **Lead investor:** [Name]
- **Co-investors:** [Names]
- **Total funding:** $[X]M
- **Source:** [Publication Name (Month Year)](URL)

**Change to existing profile:** Update line from `$[old amount]M` to `$[new amount]M`
```

---

### Regulatory Update Template

```markdown
**[Regulation Name] — Update**

- **Jurisdiction:** [Country / Region]
- **Update type:** [New regulation / Amendment / New effective date / New guidance]
- **Effective date:** [Date]
- **Summary of change:** [1-2 sentences]
- **Key AI provisions:** [Bullet points]
- **Official source:** [Official document title](Official URL)
- **Analysis source (optional):** [Secondary analysis](URL)
```

---

## Review Process

1. **Submission received** — Issues and PRs acknowledged within 72 hours
2. **Source verification** — Maintainer verifies all source URLs against METHODOLOGY.md standards
3. **Accuracy check** — Data checked against at least one cross-reference source
4. **Format review** — Contribution reviewed for consistency with existing file formatting
5. **Merge or feedback** — Accepted contributions merged; others returned with specific feedback
6. **CHANGELOG update** — Merged contributions noted in CHANGELOG.md

**Expected review time:** 3–7 business days for standard contributions; 1–2 business days for urgent corrections (e.g., vendor acquired or shut down).

---

## Vendor Disclosure Policy

If you are a vendor listed in this index and wish to update your own profile:
- You are welcome to submit corrections to factual data (funding amounts, HQ, founding year) with primary sources
- Capability descriptions will be fact-checked against independent sources; vendor-supplied capability claims require corroboration
- Please disclose your affiliation in the issue or PR description
- Contributions from vendors to their own profiles are accepted under the same standards as community contributions

---

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By contributing, you agree to abide by its terms. In summary:

- Be respectful and constructive
- No harassment, discrimination, or hostile behavior
- Focus on the data and sources, not the people
- Commercial interests are fine; they must be disclosed

---

## Contact

- **Issues:** [GitHub Issues](https://github.com/alpha-one-index/ai-trism-index/issues)
- **Organization:** [Alpha One Index](https://github.com/alpha-one-index)
- **Related repo:** [ai-infra-index](https://github.com/alpha-one-index/ai-infra-index)

---

*Thank you for helping maintain the AI TRiSM Market Index as a reliable, open-source reference for the global AI TRiSM community.*

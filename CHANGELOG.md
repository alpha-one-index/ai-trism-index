# Changelog

All notable changes to the AI TRiSM Market Index are documented here.

This project follows [Semantic Versioning](https://semver.org/):
- **Major (x.0.0):** Structural changes to repository format or methodology
- **Minor (1.x.0):** New files, new categories, new vendor profiles
- **Patch (1.0.x):** Data updates, corrections, vendor profile updates

---

### Auto-Refresh -- 2026-03-12

- Vendor websites checked: 84 total, 65 live, 11 unreachable
- Data files refreshed via automated pipeline


### Auto-Refresh -- 2026-03-11

- Vendor websites checked: 84 total, 65 live, 11 unreachable
- Data files refreshed via automated pipeline


### Auto-Refresh -- 2026-03-10

- Vendor websites checked: 84 total, 65 live, 11 unreachable
- Data files refreshed via automated pipeline


### Auto-Refresh -- 2026-03-09

- Vendor websites checked: 84 total, 65 live, 11 unreachable
- Data files refreshed via automated pipeline


### Auto-Refresh -- 2026-03-08

- Vendor websites checked: 84 total, 65 live, 11 unreachable
- Data files refreshed via automated pipeline


### Auto-Refresh -- 2026-03-07

- Vendor websites checked: 84 total, 65 live, 11 unreachable
- Data files refreshed via automated pipeline


### Auto-Refresh -- 2026-03-06

- Vendor websites checked: 84 total, 66 live, 10 unreachable
- Data files refreshed via automated pipeline


## [1.0.0] — 2026-03-01

### Initial Release

The first public release of the AI TRiSM Market Index by [Alpha One Index](https://github.com/alpha-one-index). This is the second index in the Alpha One Index project, following [ai-infra-index](https://github.com/alpha-one-index/ai-infra-index).

---

### Added

#### Core Documentation
- **README.md** — Full market overview with badge set (License MIT, Data Auto Updated Hourly, Vendors: 60+, Categories: 10, Version: 1.0.0, Data Validation: Self_Auditing, Croissant: ML_Metadata, Provenance: Documented); Q&A headings; multi-analyst market size table; top vendor tables; Gartner four-layer framework summary; repository structure; quick links; data provenance section; 8-question FAQ
- **METHODOLOGY.md** — Four-tier verification framework (Tier 1: Vendor sources; Tier 2: Analyst cross-reference; Tier 3: Regulatory sources; Tier 4: Funding verification); update schedule; staleness policy; data quality levels; error handling; versioning policy
- **CONTRIBUTING.md** — Contribution guidelines; data quality standards; vendor profile template; funding update template; regulatory update template; review process; vendor disclosure policy
- **CHANGELOG.md** — This file
- **LICENSE** — MIT License

#### Spec Files (8 files)

- **specs/vendor-profiles.md** — 60+ vendor profiles across 10 categories: AI Governance (15 vendors), AI Runtime Security (10 vendors), AI Explainability & Fairness (7 vendors), AI Red Teaming & Security Testing (6 vendors), AI Model Monitoring & Observability (7 vendors), AI Data Privacy & Protection (6 vendors), AI Content Safety & Moderation (5 vendors), AI Compliance/Regulatory Platforms (5 vendors), Large Cloud Vendor TRiSM Solutions (4 vendors), Emerging & Specialist Vendors (27 vendors); M&A activity summary table. All profiles include funding history, capabilities, customers, pricing, and source URLs.

- **specs/market-sizing.md** — Market size analysis from 8 analyst firms (Precedence Research, Research and Markets, MarketsandMarkets, Polaris Market Research, Allied Market Research, Market.us, Business Research, Analytics Canada); multi-analyst CAGR comparison; AI Governance sub-market sizing; market segment breakdowns by component, technology, application, deployment model, organization size, industry vertical, and product type; North America, Europe, and Asia-Pacific regional analysis; primary market drivers; investment and funding landscape; M&A summary; adjacent market benchmarks; analyst predictions for 2025–2030.

- **specs/regulatory-landscape.md** — Complete global regulatory landscape: EU AI Act (full text, compliance timeline, four risk tiers, provider and deployer obligations, GPAI model obligations, enforcement and penalties); NIST AI RMF 1.0/2.0 (four core functions: GOVERN, MAP, MEASURE, MANAGE); NIST AI 600-1 GenAI Profile (12 GenAI risk categories); ISO/IEC 42001 (structure, Annex A controls, relationship to other standards); ISO/IEC 23894; US Federal AI policy (Biden EO 14110, Trump January 2025 EO, Trump December 2025 EO); US state AI laws (Colorado SB 205, California AB 2013, NYC Local Law 144, Texas TRAIGA, Virginia HB 2481, others); China AI regulations (Algorithm Recommendation, Deep Synthesis, Generative AI Measures); industry-specific regulations (SR 11-7, SS1/23, DORA, GDPR Art. 22, FDA SaMD, HIPAA); global comparison matrix; regulatory timeline 2018–2030.

- **specs/gartner-framework.md** — Gartner AI TRiSM definition and origins; complete four-layer framework (Layer 1: AI Governance; Layer 2: AI Runtime Inspection & Enforcement; Layer 3: Information Governance; Layer 4: Infrastructure & Stack); four mandatory features (AI catalog, continuous evaluation, runtime inspection, provider independence); four key market trends (market segments, agentic AI controls, TRiSM-as-a-Service, GenAI risks); 2025 Market Guide publication details; Market Guide vs. Magic Quadrant comparison; Gartner 2025 Representative Vendors (confirmed via press releases); Gartner Cool Vendors in Agentic AI TRiSM (September 2, 2025); Hype Cycle positioning (Peak of Inflated Expectations 2025); key Gartner statistics; framework comparison with related frameworks; 4-phase implementation path; cross-functional responsibility matrix.

- **specs/platform-comparison.md** — Head-to-head feature matrices for AI Governance, AI Runtime Security, AI Model Monitoring, AI Data Privacy, and AI Red Teaming categories; decision framework by buyer type, budget size, and Gartner layer priority; pricing model comparison (usage-based, enterprise SaaS, platform bundle, open source + commercial); deployment model matrix (cloud, on-premises, hybrid, marketplace availability); regulatory framework coverage matrix (EU AI Act, NIST AI RMF, ISO 42001, GDPR, CCPA, SR 11-7, SS1/23, HIPAA, NAIC); Gartner four-layer coverage matrix for all vendors; platform consolidation leaders.

- **specs/ma-activity.md** — Complete acquisition table (8 deals; $1.905B+ confirmed value); deep dives on all major acquisitions: Veeam/Securiti AI ($1.725B), F5/CalypsoAI ($180M), Cisco/Robust Intelligence, Coralogix/Aporia, SentinelOne/Prompt Security, Cato Networks/Aim Security, Palo Alto Networks/Protect AI, Apple/WhyLabs; funding rounds table (11 rounds, $400M+ tracked); strategic investor analysis; five forces driving consolidation; acquirer pattern analysis by type; strategic implications of major deals; M&A pipeline outlook; acquisition target probability analysis; AI TRiSM investment vs. broader AI security context.

- **specs/implementation-guide.md** — 4-phase implementation playbook: Phase 1 Foundation (AI catalog, governance structure, risk classification, basic info governance); Phase 2 Evaluation (pre-deployment evaluation, model documentation, runtime inspection, SIEM integration); Phase 3 Advanced Controls (continuous monitoring, agentic AI controls, regulatory compliance automation, provider independence); Phase 4 Optimization (platform consolidation, advanced DSPM, culture); AI TRiSM maturity model (4 levels); self-assessment checklist; framework selection guide; tool selection criteria matrix; tool selection by phase; cross-functional RACI matrix; cost estimates by organization size; cost-benefit analysis framework; common implementation mistakes; business case template; open source resource list.

- **specs/agentic-ai-security.md** — Agentic AI definition and why it is a distinct field; comparison of static GenAI vs. agentic AI risk dimensions; scale of enterprise agent deployment (80% of Fortune 500 per Gartner/Zenity); core agentic AI threat taxonomy (indirect prompt injection, privilege escalation, memory corruption, tool call hijacking, multi-agent coordination exploitation, denial of service); Gartner Cool Vendors in Agentic AI TRiSM (Zenity, Aim Security, vijil) with full profiles; three core access control problems (coarse-grained authorization, no standard identity framework, dynamic permission escalation); principle of least privilege for AI agents; technical explanation of indirect prompt injection with real-world examples; AgentFlayer zero-click exploit chain (Zenity Labs, August 2025); defense-in-depth architecture pattern; attack surface by enterprise agent type; compound agent risk in multi-agent systems; immediate and short-term implementation recommendations; agentic AI security market outlook and key vendors to watch.

---

### Data Provenance

All data in this initial release is sourced from the following primary research:
- Vendor funding: PR Newswire, Business Wire, GlobeNewswire, TechCrunch, VentureBeat press releases (2022–2026)
- Market sizing: Precedence Research, Research and Markets, MarketsandMarkets, Polaris Market Research, Allied Market Research, Market.us, Business Research (via Yahoo Finance), Analytics Canada reports
- Gartner recognition: Vendor press releases citing Gartner Market Guide for AI TRiSM (February 18, 2025) and Gartner Cool Vendors in Agentic AI TRiSM (September 2, 2025)
- Regulatory data: EU Official Journal, NIST AI Resource Center (airc.nist.gov), ISO.org, White House official publications, Federal Reserve, NCSL, FDA, HHS, CAC
- M&A data: TechCrunch, CyberScoop, SecurityWeek, Channel Futures, FinTech Global

**Research cutoff date:** March 2026

---

## Upcoming

The following updates are planned for future releases:

- `v1.1.0` — Addition of vendor profiles for Patronus AI, EQTY Lab, Vals AI, and other emerging governance specialists
- `v1.1.0` — Addition of Forrester Wave AI Governance data when next Wave publishes
- `v1.2.0` — EU AI Act August 2026 compliance deadline tracking and impact analysis
- `v1.2.0` — Addition of IDC MarketScape for AI Governance analysis
- `v1.3.0` — Gartner 2026 Market Guide for AI TRiSM update (expected Q1 2026)

---

[Unreleased]: https://github.com/alpha-one-index/ai-trism-index/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/alpha-one-index/ai-trism-index/releases/tag/v1.0.0

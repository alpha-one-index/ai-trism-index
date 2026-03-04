# AI Agentic Governance & Security (A2GS) Index

> The first comprehensive open-source index mapping AI agent security vendors, OWASP Agentic Top 10 mitigations, framework vulnerabilities, MCP supply chain risks, and market forecasts. An extension of the [AI TRiSM Market Index](../README.md).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![OWASP: Agentic Top 10 2026](https://img.shields.io/badge/OWASP-Agentic_Top_10_2026-red)](owasp-agentic-top10.md)
[![Vendors: 30+](https://img.shields.io/badge/Vendors-30+-blue)](vendors.csv)
[![Standards: 6](https://img.shields.io/badge/Standards-6-orange)](standards.md)

## Why A2GS?

- 81% of enterprise teams deployed agents past planning phase; only 14.4% have full security approval (Gravitee State of AI Agent Security 2026)
- OWASP released the first Top 10 for Agentic Applications in 2026 — 10 novel risk categories absent from traditional AI security
- Forbes predicts a major public agentic AI breach in 2026 (Forbes, Dec 2025)
- Gartner published inaugural Cool Vendors in Agentic AI TRiSM (September 2025)
- No comprehensive structured index existed for this space — until now

## Contents

| File | Description |
|------|-------------|
| [owasp-agentic-top10.md](owasp-agentic-top10.md) | OWASP Top 10 for Agentic Applications 2026 with vendor mitigation mapping and coverage heat map |
| [vendors.csv](vendors.csv) | 30+ agentic security vendors: funding, capabilities, OWASP risks addressed |
| [frameworks-at-risk.md](frameworks-at-risk.md) | Agent frameworks (LangChain, CrewAI, AutoGen, LangGraph, OpenAI Agents SDK, Replit) with known vulns and risk ratings |
| [standards.md](standards.md) | OWASP AIVSS, NIST AI RMF agentic extensions, CSA AICM, EU AI Act agent provisions, ISO/IEC 42001 |
| [mcp-security.md](mcp-security.md) | Model Context Protocol supply chain risks, malicious server incidents, authentication patterns |
| [market-data.json](market-data.json) | Agent security market forecasts 2025-2035 from multiple analyst firms |

## Structured Data

| File | Format | Description |
|------|--------|-------------|
| [../data/agentic-vendors.json](../data/agentic-vendors.json) | JSON | Machine-readable vendor profiles with nested capabilities |
| [vendors.csv](vendors.csv) | CSV | Flat vendor data for spreadsheet/database import |

## Related Specs

- [specs/agentic-ai-security.md](../specs/agentic-ai-security.md) — Deep-dive risk taxonomy, Gartner Cool Vendor profiles (Zenity, vijil, Aim Security), AgentFlayer attack analysis, defense-in-depth architecture, implementation recommendations
- [specs/vendor-profiles.md](../specs/vendor-profiles.md) — Full AI TRiSM vendor profiles (60+)
- [specs/regulatory-landscape.md](../specs/regulatory-landscape.md) — EU AI Act, NIST AI RMF, ISO/IEC 42001 regulatory tracking
- [specs/gartner-framework.md](../specs/gartner-framework.md) — Gartner four-layer AI TRiSM framework analysis

## Key Statistics

| Metric | Value | Source |
|--------|-------|--------|
| Enterprise teams with agents deployed | 81% past planning | Gravitee 2026 Report |
| Teams with full agent security approval | 14.4% | Gravitee 2026 Report |
| Gartner forecast: agent attacks via access control | 50%+ by 2029 | Gartner via Prompt Security |
| Fortune 500 deploying agents in production | 80%+ | Zenity Labs Research 2025 |
| OWASP Agentic risk categories | 10 | OWASP Top 10 Agentic 2026 |

## Sources

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Gravitee State of AI Agent Security 2026](https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control)
- [CyberArk AI Agent Security Market 2026](https://www.cyberark.com/resources/blog/whats-shaping-the-ai-agent-security-market-in-2026)
- [Forbes Agentic AI 2026 Predictions](https://www.forbes.com/sites/markminevich/2025/12/31/agentic-ai-takes-over-11-shocking-2026-predictions/)
- [CSA Agentic AI Predictions 2026](https://cloudsecurityalliance.org/blog/2026/01/16/my-top-10-predictions-for-agentic-ai-in-2026)
- [Gartner Cool Vendors in Agentic AI TRiSM (Sep 2025)](https://zenity.io/blog/current-events/zenity-named-a-2025-cool-vendor-in-gartner-s-agentic-ai-trism-report)
- [Palo Alto OWASP Agentic Analysis](https://www.paloaltonetworks.com/blog/cloud-security/owasp-agentic-ai-security/)

## Citation

See [CITATION.cff](../CITATION.cff) for how to cite this index.

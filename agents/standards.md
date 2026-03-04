# Agentic AI Security Standards & Regulatory Frameworks

> Comprehensive mapping of standards, frameworks, and regulations applicable to autonomous AI agent governance. Complements [specs/regulatory-landscape.md](../specs/regulatory-landscape.md) with agent-specific provisions.

**Last updated:** March 2026

---

## Standards Overview

| Standard | Organization | Status | Agent-Specific | Scope |
|----------|-------------|--------|:--------------:|-------|
| **OWASP Top 10 for Agentic Applications** | OWASP | Released 2026 | Yes | 10 critical security risks for autonomous AI agents |
| **OWASP AIVSS** | OWASP | In development | Yes | AI Vulnerability Scoring System for standardized risk rating |
| **NIST AI RMF 1.0** | NIST | Released Jan 2023 | Partial | AI risk management framework; agentic extensions emerging |
| **NIST AI 600-1** | NIST | Released Jul 2024 | Partial | Generative AI risk profile; agent risks referenced |
| **CSA AICM** | Cloud Security Alliance | Released 2025 | Yes | AI Controls Matrix for cloud-deployed AI systems including agents |
| **EU AI Act** | European Union | Effective Aug 2025 | Partial | High-risk AI system requirements; agent obligations emerging |
| **ISO/IEC 42001** | ISO/IEC | Released Dec 2023 | Partial | AI management system standard; governance framework |
| **ISO/IEC 27090** | ISO/IEC | In development | Yes | AI cybersecurity guidance; agent threat models |

---

## 1. OWASP Top 10 for Agentic Applications 2026

**URL:** [genai.owasp.org](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

The first globally peer-reviewed framework identifying critical security risks for autonomous AI agents. Developed by 100+ experts. Covers 10 risk categories from agent goal hijacking to rogue agents.

**Agent-Specific Provisions:**
- Defines risks unique to autonomous systems (tool misuse, inter-agent communication, cascading failures)
- Provides real-world attack examples for each risk
- Framework for vendor evaluation against agentic risks

See [owasp-agentic-top10.md](owasp-agentic-top10.md) for full mapping.

## 2. OWASP AIVSS (AI Vulnerability Scoring System)

**Status:** In development (2026)

Standardized scoring system for AI vulnerabilities, analogous to CVSS for software vulnerabilities. Will enable consistent risk rating across agentic AI systems.

**Key Features:**
- Severity scoring for AI-specific attack vectors (prompt injection, memory poisoning)
- Agent autonomy level as a risk multiplier
- Tool access scope as an impact factor

**Source:** [CSA Agentic AI Predictions 2026](https://cloudsecurityalliance.org/blog/2026/01/16/my-top-10-predictions-for-agentic-ai-in-2026)

## 3. NIST AI Risk Management Framework (AI RMF)

**URL:** [nist.gov/ai](https://www.nist.gov/artificial-intelligence)

NIST AI RMF 1.0 provides a voluntary framework for managing AI risks. While not agent-specific, its four core functions (Govern, Map, Measure, Manage) apply directly to agentic AI governance.

**Agentic Extensions (Emerging):**
- NIST AI 600-1 (Generative AI Profile) references autonomous system risks
- Community working groups developing agentic-specific controls
- Aligns with CSA AICM for cloud-deployed agents

**Agent Application:**
- Govern: Establish agent security policies and approval workflows
- Map: Inventory all deployed agents, their tools, and data access
- Measure: Continuous evaluation of agent behavior against baselines
- Manage: Incident response for agent compromise; kill switches

## 4. CSA AI Controls Matrix (AICM)

**Organization:** Cloud Security Alliance
**Status:** Released 2025

The AI Controls Matrix provides security controls for cloud-deployed AI systems, with specific provisions for agentic architectures.

**Agent-Specific Controls:**
- Agent identity and access management
- Multi-agent communication security
- Agent lifecycle governance (build, deploy, monitor, retire)
- Runtime behavioral monitoring requirements

**Source:** [CSA Agentic AI Predictions 2026](https://cloudsecurityalliance.org/blog/2026/01/16/my-top-10-predictions-for-agentic-ai-in-2026)

## 5. EU AI Act — Agent Provisions

**Effective:** August 2025 (phased implementation through 2027)

The EU AI Act classifies AI systems by risk level. Autonomous AI agents that make decisions affecting individuals will likely fall under high-risk or general-purpose AI system requirements.

**Agent-Relevant Obligations:**
- Transparency: Users must be informed they are interacting with an AI agent
- Human oversight: High-risk agent systems require human-in-the-loop or human-on-the-loop
- Risk management: Continuous risk assessment for deployed agent systems
- Logging: Comprehensive audit trails for agent actions (aligns with OWASP R8 cascading failures)
- Conformity assessment: Before deployment of high-risk agent systems

**Timeline:**
- Aug 2025: Prohibited AI practices take effect
- Aug 2026: GPAI model obligations; high-risk classification rules
- Aug 2027: Full enforcement of all high-risk AI system requirements

## 6. ISO/IEC 42001 — AI Management System

**Released:** December 2023

Provides requirements for establishing, implementing, and improving an AI management system. Applicable to organizations deploying AI agents at enterprise scale.

**Agent Governance Application:**
- Policy framework for agent deployment approval
- Risk assessment methodology for agent capabilities
- Continuous improvement cycle for agent security controls
- Third-party agent/tool supply chain management

---

## Standards Alignment Matrix

| Requirement | OWASP Agentic | NIST AI RMF | CSA AICM | EU AI Act | ISO 42001 |
|-------------|:---:|:---:|:---:|:---:|:---:|
| Agent inventory/discovery | . | X | X | X | X |
| Runtime behavioral monitoring | X | . | X | . | . |
| Tool access controls | X | . | X | . | . |
| Human oversight gates | X | X | . | X | X |
| Audit trail/logging | X | X | X | X | X |
| Incident response | . | X | X | . | X |
| Supply chain security | X | . | X | . | X |
| Inter-agent communication security | X | . | X | . | . |
| Risk assessment | X | X | X | X | X |
| Transparency/explainability | X | X | . | X | X |

---

## Sources

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence)
- [CSA Agentic AI Predictions 2026](https://cloudsecurityalliance.org/blog/2026/01/16/my-top-10-predictions-for-agentic-ai-in-2026)
- [EU AI Act Official Text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)

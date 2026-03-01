# AI TRiSM Regulatory Landscape

> Complete guide to global AI regulations, compliance frameworks, and industry-specific requirements for AI TRiSM programs. All data sourced inline. Last updated: March 2026.

---

## Table of Contents

1. [What Is the EU AI Act?](#1-what-is-the-eu-ai-act)
2. [What Is the NIST AI Risk Management Framework?](#2-what-is-the-nist-ai-risk-management-framework)
3. [What Is ISO/IEC 42001 and How Does It Apply to AI?](#3-what-is-isoiec-42001-and-how-does-it-apply-to-ai)
4. [What Are AI TRiSM Compliance Frameworks?](#4-what-are-ai-trism-compliance-frameworks)
5. [What Is US Federal AI Policy?](#5-what-is-us-federal-ai-policy)
6. [What Are US State AI Laws?](#6-what-are-us-state-ai-laws)
7. [What Are China's AI Regulations?](#7-what-are-chinas-ai-regulations)
8. [What Are Industry-Specific AI Regulations?](#8-what-are-industry-specific-ai-regulations)
9. [How Do Global AI Regulations Compare?](#9-how-do-global-ai-regulations-compare)
10. [What Is the Global AI Regulatory Timeline?](#10-what-is-the-global-ai-regulatory-timeline)

---

## 1. What Is the EU AI Act?

### Overview

The EU Artificial Intelligence Act (Regulation (EU) 2024/1689) is the world's first comprehensive horizontal AI regulation. It entered into force on **August 2, 2024**, following publication in the Official Journal of the European Union. The Act establishes a risk-based tiered framework that imposes obligations commensurate with the potential harm of AI systems.

**Full text:** [EUR-Lex — Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)

The EU AI Act is the most consequential piece of AI legislation globally — it applies to any organization placing AI systems on the EU market or using AI systems to affect EU residents, regardless of where the organization is headquartered. This means US, Chinese, and all other non-EU companies providing AI services to EU customers must comply.

---

### 1.1 Compliance Timeline

| Milestone | Date | Description |
|-----------|------|-------------|
| Regulation enters into force | **August 2, 2024** | 20 days after publication in the EU Official Journal |
| Prohibited AI systems ban | **February 2, 2025** | 6-month transition: Unacceptable-risk AI banned (Article 5) |
| GPAI obligations — new systems | **August 2, 2025** | 12-month: General-Purpose AI model rules (Chapter V) apply to new systems |
| Notified body accreditation | **August 2, 2026** | Member States complete conformity assessment infrastructure |
| **High-risk AI operators compliance** | **August 2, 2026** | 24-month: Most high-risk AI obligations apply to operators/deployers |
| Full compliance — existing GPAI | **August 2, 2027** | GPAI models already on market must comply with Chapter V |
| Medical devices / critical infrastructure | **August 2, 2027** | High-risk AI embedded in regulated products |
| Large-scale IT system AI | **December 31, 2030** | AI in Annex X systems placed on market before Aug 2027 |

**Sources:** [DataGuard EU AI Act Timeline](https://www.dataguard.com/eu-ai-act/timeline), [Parva Consulting Compliance Deadlines](https://parvaconsulting.com/articles/eu-ai-act-governance-compliance-deadlines-business-impact/)

---

### 1.2 Risk Tier Classification

The Act classifies AI systems into four risk tiers:

#### Tier 1: Unacceptable Risk (Prohibited) — Article 5

As of **February 2, 2025**, the following AI systems are **banned in the EU**:

| Prohibited Application | Description |
|------------------------|-------------|
| Real-time remote biometric ID in public spaces | Law enforcement use — with narrow exceptions for serious crimes |
| Social scoring by public authorities | Government systems rating citizens based on behavior |
| Exploiting vulnerabilities of specific groups | Based on age, disability, or social situation |
| Subliminal manipulation | Techniques that bypass conscious decision-making |
| Emotion recognition in workplaces/education | AI reading emotional states of employees or students |
| Biometric categorization by sensitive characteristics | Race, political opinions, religious beliefs, sexual orientation |
| Predictive policing based solely on profiling | Without objective, individual-level criminal indicators |

**Source:** [EU AI Act Article 5 — artificialintelligenceact.eu](https://artificialintelligenceact.eu/article/5/)

---

#### Tier 2: High Risk — Annex III + Annex II

**Annex III — High-Risk Use Cases (8 categories):**

| Category | Examples |
|----------|---------|
| 1. Biometric identification | Systems used to identify, verify, or categorize natural persons |
| 2. Critical infrastructure | AI managing energy, water, transport, gas — where malfunction endangers life |
| 3. Education / vocational training | AI determining access to education, admissions, exam scoring |
| 4. Employment | AI in recruitment, performance evaluation, promotion, task allocation |
| 5. Essential services | AI for credit scoring, life/health insurance risk assessment |
| 6. Law enforcement | Risk assessment of individuals, polygraph, evidence evaluation |
| 7. Migration / border control | Risk assessment of persons, asylum claim examination |
| 8. Justice / democratic processes | AI assisting courts; electoral influence systems |

**Annex II** covers AI systems embedded in regulated products (medical devices, machinery, vehicles, aviation, marine, rail equipment, radio equipment) that were already subject to third-party conformity assessment.

**Source:** [ModelOp EU AI Act Summary](https://www.modelop.com/ai-governance/ai-regulations-standards/eu-ai-act), [Latham & Watkins Deployer Obligations](https://www.lw.com/en/insights/eu-ai-act-obligations-for-deployers-of-high-risk-ai-systems)

---

#### Tier 3: Limited Risk

Transparency obligations only — no conformity assessment required:

- **Chatbots:** Must disclose they are AI (unless obviously a bot)
- **Deep fakes:** Must be labeled as artificially generated or manipulated
- **AI-generated text published for public interest:** Must be labeled as AI-generated

---

#### Tier 4: Minimal Risk

No mandatory requirements. Voluntary codes of conduct encouraged. Encompasses the vast majority of AI applications — spam filters, AI in video games, AI-enabled inventory management, recommendation systems (non-essential), etc.

---

### 1.3 High-Risk AI Provider Obligations

Providers (developers/manufacturers) placing high-risk AI on the EU market must:

| Obligation | Description |
|-----------|-------------|
| Risk Management System | Documented risk management process throughout AI system lifecycle |
| Data Governance | Training/validation/testing data: relevant, representative, error-free, complete |
| Technical Documentation | Annex IV-compliant documentation sufficient for conformity assessment |
| Record-Keeping | Automatic event logging for post-market monitoring and incident investigation |
| Transparency / Instructions for Use | Clear documentation for downstream deployers enabling compliance |
| Human Oversight | Design systems to allow effective human oversight with appropriate interfaces |
| Accuracy, Robustness, Cybersecurity | Appropriate levels; resilience against errors, faults, adversarial attacks |
| Quality Management System | Formal QMS including policies, procedures, and responsibilities |
| Conformity Assessment | Self-assessment or third-party notified body review before market placement |
| EU Declaration + CE Marking | Issue declaration and affix CE marking |
| Registration | Register in the EU AI database (Article 71) |
| Post-Market Monitoring | Monitoring plan; report serious incidents within 15 days (2 days if life-threatening) |

**Source:** [ModelOp High-Risk Provider Obligations](https://www.modelop.com/ai-governance/ai-regulations-standards/eu-ai-act)

---

### 1.4 High-Risk AI Deployer Obligations

Deployers (organizations using AI systems in professional contexts) must:

| Obligation | Description |
|-----------|-------------|
| AI Literacy Training | Ensure all users have sufficient AI knowledge to use systems as intended |
| Human Oversight Assignment | Assign competent persons with authority to oversee AI operation |
| Technical & Organizational Measures | Ensure use aligns with provider's instructions for use |
| Input Data Quality | Where controlling input data: ensure it is relevant, qualitative, representative |
| Log Retention | Maintain automatically generated logs for at least 6 months |
| Continuous Monitoring | Monitor for risks; detect anomalies and unexpected performance |
| Incident Notification | Inform providers and market surveillance authorities of serious incidents without delay |
| Suspension Obligation | Suspend use immediately if AI poses risk |
| Fundamental Rights Impact Assessment (FRIA) | Required for: public authorities, banks, insurers, and employers |
| Transparency to Individuals | Inform natural persons they are subject to a high-risk AI system |
| Workforce Information | Inform workers and representatives before deploying AI in the workplace |
| Authority Cooperation | Cooperate fully with national competent authorities |

**Source:** [EU AI Act Article 26](https://artificialintelligenceact.eu/article/26/), [Latham & Watkins Deployer Obligations](https://www.lw.com/en/insights/eu-ai-act-obligations-for-deployers-of-high-risk-ai-systems)

---

### 1.5 General-Purpose AI (GPAI) Model Obligations

All GPAI providers (models like GPT-4, Claude, Gemini, Llama) must (from August 2, 2025 for new systems):

| All GPAI Providers | Additional for Systemic Risk (>10²⁵ FLOPs) |
|-------------------|---------------------------------------------|
| Maintain up-to-date technical documentation | Notify European Commission |
| Provide info/documentation to downstream providers | Model evaluation per standardized protocols including adversarial testing |
| Policy to respect EU copyright law | Assess and mitigate systemic risks |
| Publish summary of training data | Report serious incidents to Commission within 2 days |
| — | Implement cybersecurity proportionate to risk |

**Source:** [ModelOp EU AI Act Summary](https://www.modelop.com/ai-governance/ai-regulations-standards/eu-ai-act)

---

### 1.6 Enforcement and Penalties

| Violation | Maximum Penalty |
|-----------|----------------|
| Prohibited AI practices (Tier 1 violations) | **€35,000,000 or 7% of global annual turnover** |
| Other violations of the Regulation | €15,000,000 or 3% of global annual turnover |
| Providing incorrect/misleading information | €7,500,000 or 1.5% of global annual turnover |
| SME/startup | Lower of the two caps applies (proportionality) |

**Enforcement structure:**
- **National Market Surveillance Authorities (MSAs)** in each EU member state handle enforcement
- **EU AI Office** (within European Commission) has direct supervisory authority over GPAI model providers
- **Whistleblower protection** included for those reporting violations

**Source:** [DataGuard EU AI Act Timeline](https://www.dataguard.com/eu-ai-act/timeline)

---

## 2. What Is the NIST AI Risk Management Framework?

### 2.1 Overview

The **NIST AI Risk Management Framework (AI RMF)** is a voluntary framework developed by the US National Institute of Standards and Technology. While not legally binding, it is the most influential voluntary AI governance standard in the US and increasingly globally — adopted by reference in Colorado SB 205, used by federal agencies under OMB guidance, and informing ISO/IEC 42001.

| Document | Published | Key Content |
|----------|-----------|-------------|
| **AI RMF 1.0** | January 26, 2023 | Core four-function framework: GOVERN, MAP, MEASURE, MANAGE |
| **AI RMF 2.0** | February 2024 | Updated with expanded guidance on specific AI risk categories |
| **NIST AI 600-1 GenAI Profile** | July 26, 2024 | Companion for generative AI; 12 high-level GenAI risk categories |

**Source:** [NIST AI RMF Official Page](https://airc.nist.gov/Home), [ModelOp NIST AI RMF Summary](https://www.modelop.com/ai-governance/ai-regulations-standards/nist-ai-rmf)

---

### 2.2 The Four Core Functions

#### GOVERN

**Purpose:** Create organizational structures, policies, and culture for AI risk accountability.

Key activities:
- Define clear ownership for every AI system in use
- Establish cross-functional AI review structures (AI governance committee, ethics board)
- Align on risk tolerance and mitigation thresholds
- Implement recurring evaluations of risk metrics and governance health
- Train teams across functions in AI risk fluency
- Ensure legal and regulatory requirements are understood and documented
- Create processes for incident disclosure and response
- Oversee downstream AI adoption, use, and decommissioning

**Note:** GOVERN is the only function that operates across the entire AI lifecycle — it provides the authority and accountability structure for the other three functions.

---

#### MAP

**Purpose:** Establish context for identifying and categorizing AI risks before and during deployment.

Key activities:
- Inventory all AI systems in use (including third-party embedded AI)
- Document intended uses, beneficial uses, and deployment context
- Identify applicable laws, regulations, and stakeholder expectations
- Classify AI systems by risk tier (low/medium/high) based on data sensitivity, decision consequences, regulatory impact, and model complexity
- Identify potential harms to individuals, organizations, and society
- Define what data is ingested and what decisions are influenced

---

#### MEASURE

**Purpose:** Develop and apply processes to evaluate, characterize, and prioritize AI risks.

Key activities:
- Evaluate for bias and fairness across demographic subpopulations
- Assess explainability — can decisions be explained to users and regulators?
- Conduct adversarial testing and threat modeling
- Validate, explain, and document AI inputs and outputs
- Assess cybersecurity and resilience vulnerabilities
- Benchmark model performance against established metrics
- Continuous monitoring for model drift and performance degradation
- Quantify uncertainty in model outputs

---

#### MANAGE

**Purpose:** Prioritize and treat identified risks through controls, monitoring, and response.

Key activities:
- Implement human-in-the-loop controls for high-impact decisions
- Apply access controls to sensitive training and inference data
- Create model documentation (model cards, datasheets, lineage maps)
- Deploy live monitoring for performance drift and anomalous outputs
- Implement user-facing explainability tools
- Establish escalation paths and incident response procedures
- Regularly review and update risk controls as systems evolve
- Decommission AI systems that cannot be adequately managed

**Source:** [Lumenova AI — NIST AI RMF Guide](https://www.lumenova.ai/blog/ai-risk-assessment-best-practices-nist-ai-rmf/), [Reed Smith NIST AI 600-1 Analysis](https://www.reedsmith.com/articles/managing-genai-takeaways-nist-guidance-responsible-genai-implementation/)

---

### 2.3 NIST AI 600-1: GenAI Profile (July 26, 2024)

Published July 26, 2024, the GenAI Profile is a companion to AI RMF 1.0 specifically addressing risks unique to Generative AI systems. Mandated by Biden Executive Order 14110 (October 2023).

**12 High-Level GenAI Risk Categories:**

| # | Risk Category | Description |
|---|---------------|-------------|
| 1 | CBRN Uplift | Access to knowledge enabling chemical, biological, radiological, or nuclear weapons |
| 2 | Confabulation | Generation of factually incorrect outputs (hallucinations) presented with confidence |
| 3 | Data Privacy | Unauthorized reproduction of training data containing personal information |
| 4 | Human-AI Configuration | Automation bias, over-reliance, or emotional entanglement with GenAI |
| 5 | Information Integrity | Difficulty distinguishing AI-generated fact from fiction; misinformation |
| 6 | Information Security | Lowered barriers for offensive cyber capabilities (malware, phishing) |
| 7 | Intellectual Property | Unauthorized production of copyrighted, trademarked, or licensed content |
| 8 | Obscene/Abusive Content | Generation of degrading, harmful, or CSAM-adjacent content |
| 9 | Value Chain Integration | Difficulty vetting AI suppliers; third-party risk in AI pipelines |
| 10 | Data Provenance | Inability to verify training data origins; contamination risks |
| 11 | Socioeconomic Impacts | Workforce displacement; concentration of AI capability |
| 12 | Environmental Impact | Energy consumption and resource use by large GenAI models |

**Source:** [Reed Smith NIST AI 600-1 Analysis](https://www.reedsmith.com/articles/managing-genai-takeaways-nist-guidance-responsible-genai-implementation/), [LinkedIn NIST AI 600-1 Guide](https://www.linkedin.com/pulse/understanding-nist-ai-600-1-framework-comprehensive-guide-singh-0xq2c)

---

### 2.4 NIST AI RMF Regulatory Influence

| Regulation/Framework | NIST AI RMF Role |
|---------------------|-----------------|
| Colorado SB 205 | Compliance with NIST AI RMF cited as evidence of "reasonable care" |
| EU AI Act standards | NIST AI RMF input to EU/ISO harmonization efforts |
| Federal procurement | OMB M-24-10 for federal agencies aligns with NIST AI RMF |
| FFIEC | Financial regulators reference NIST RMF for AI model risk management |
| ISO/IEC 42001 | Designed for interoperability with NIST AI RMF |

---

## 3. What Is ISO/IEC 42001 and How Does It Apply to AI?

### 3.1 Overview

**Published:** December 18, 2023
**Full Title:** Information technology — Artificial intelligence — Management system
**Type:** International Standard (certifiable, third-party auditable)

ISO/IEC 42001 is the world's first **certifiable international standard for AI Management Systems (AIMS)**. Unlike NIST AI RMF (guidance) or the EU AI Act (law), ISO/IEC 42001 enables organizations to obtain third-party certification — directly comparable to ISO 27001 (information security) or ISO 9001 (quality management).

**Source:** [ISO Official Page — ISO/IEC 42001](https://www.iso.org/standard/81230.html)

---

### 3.2 Structure: Plan-Do-Check-Act (PDCA)

| Phase | Description |
|-------|-------------|
| **Plan** | Establish AI management system scope, context, policies, objectives, and risk assessment |
| **Do** | Implement AI management controls; deploy AI systems per defined processes |
| **Check** | Monitor, measure, analyze, and evaluate performance; conduct internal audits |
| **Act** | Take corrective actions; continually improve the AIMS |

---

### 3.3 Standard Clauses (4–10)

| Clause | Title | Key Requirements |
|--------|-------|-----------------  |
| **4** | Context of the Organization | Identify internal/external issues; interested parties; scope of AIMS |
| **5** | Leadership | Top management commitment; AI policy; roles and responsibilities |
| **6** | Planning | AI risk assessment; AI impact assessment; treatment plans |
| **7** | Support | Resources; competence; awareness; communication; documentation |
| **8** | Operation | AI system lifecycle; AI impact assessment (mandatory); operational controls |
| **9** | Performance Evaluation | Monitoring; internal audit; management review |
| **10** | Improvement | Nonconformity handling; corrective actions; continual improvement |

**AI Impact Assessment (Clause 8):** A mandatory component — organizations must identify and assess potential negative impacts of AI systems on individuals, groups, and society before deployment and continuously thereafter.

---

### 3.4 Annex A Controls (38 Controls, 9 Domains)

| Domain | Controls |
|--------|---------|
| 1. AI policies | Establishing and maintaining AI-specific policies |
| 2. Internal organization | Governance structures, roles, responsibilities |
| 3. Resources for AI systems | Compute, data, and human resources |
| 4. Assessing AI systems | Risk and impact assessment procedures |
| 5. AI system lifecycle | Design through retirement governance |
| 6. Data for AI systems | Data quality, lineage, documentation |
| 7. Third-party AI | Vendor and supplier oversight |
| 8. AI system use | User information, human oversight |
| 9. Documentation | Model cards, technical documentation |

---

### 3.5 ISO/IEC 42001 vs. Related Standards

| Standard | Relationship |
|----------|-------------|
| **ISO/IEC 23894:2023** | AI risk management guidance; companion to 42001; detailed risk assessment methodology |
| **ISO/IEC 27001:2022** | Information security management; 42001 integrates with 27001 |
| **ISO 9001:2015** | Quality management; 42001 uses same PDCA structure and High-Level Structure (HLS) |
| **NIST AI RMF** | Designed for interoperability; can be used together for comprehensive governance |
| **EU AI Act** | ISO/IEC 42001 certification may support EU AI Act conformity assessment for high-risk systems |

**Source:** [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html), [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html)

---

## 4. What Are AI TRiSM Compliance Frameworks?

### Framework Comparison Matrix

| Framework | Type | Jurisdiction | Certifiable | Mandatory | Best For |
|-----------|------|-------------|-------------|-----------|---------|
| **EU AI Act** | Hard law | EU/EEA | No (but CE marking required) | Yes (for covered AI) | EU market access |
| **NIST AI RMF** | Voluntary guidance | US (global adoption) | No | No (federal agencies: yes) | US-centric governance |
| **ISO/IEC 42001** | Certifiable standard | International | **Yes** | No | Third-party attestation |
| **ISO/IEC 23894** | Guidance | International | No | No | Risk management methodology |
| **Colorado SB 205** | State law | Colorado, US | No | Yes (covered AI) | US high-risk AI |
| **GDPR Article 22** | Hard law | EU/EEA | No | Yes | Automated decision-making |
| **SR 11-7** | Supervisory guidance | US banking | No | Yes (for banks) | Financial model governance |
| **SS1/23** | Supervisory guidance | UK banking | No | Yes (for banks) | UK financial model governance |
| **DORA** | Hard law | EU financial services | No | Yes | EU financial AI resilience |
| **FDA SaMD guidance** | Regulatory guidance | US medical devices | No | Yes (for SaMD) | Medical AI |
| **China GenAI Measures** | Hard law | China | No | Yes | China market access |

### Mapping Across Frameworks

Organizations seeking comprehensive AI TRiSM compliance should implement:

1. **ISO/IEC 42001** as the overarching management system framework (certifiable baseline)
2. **NIST AI RMF** for detailed technical implementation guidance (particularly for US-focused organizations)
3. **EU AI Act** compliance for high-risk AI serving EU market (additional obligations on top of 42001)
4. **Industry-specific frameworks** (SR 11-7 for banking, FDA SaMD for medical, HIPAA for healthcare)

**Vendor tools for multi-framework compliance:** Credo AI (pre-built policy packs for EU AI Act, NIST, ISO 42001, SOC 2), IBM watsonx.governance (pre-configured frameworks for EU AI Act, ISO 42001, NIST, GDPR), Holistic AI, ValidMind (financial services)

---

## 5. What Is US Federal AI Policy?

### 5.1 Biden Administration — Executive Order 14110 (October 30, 2023)

President Biden signed **EO 14110 on "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence"** — the most comprehensive US federal AI action to that date.

**Key directives:**
- Required developers of foundational AI models to report safety test results to the federal government (Defense Production Act authority)
- Directed NIST to develop AI safety and security standards (resulting in NIST AI RMF 2.0 and AI 600-1)
- Required agencies to designate Chief AI Officers
- Directed content authentication and watermarking guidance
- Called for Congressional action on comprehensive privacy legislation
- Required agencies to address algorithmic discrimination in housing, credit, criminal justice

**Status:** **Rescinded by President Trump on January 20, 2025 (Day 1 of new administration)**

**Source:** [White House EO 14110](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/)

---

### 5.2 Trump Administration — AI Policy (2025)

#### Executive Order: "Removing Barriers to American Leadership in Artificial Intelligence" (January 20, 2025)

- Revoked Biden's EO 14110
- Directed agencies to review all Biden-era AI policies for revision or rescission within 60 days
- Emphasized reducing regulatory barriers to AI development and US AI competitiveness

**Source:** [White House January 20, 2025 EO](https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/)

---

#### Executive Order: "Ensuring a National Policy Framework for AI" (December 11, 2025)

This EO directly targeted the patchwork of state AI laws:

| Provision | Description |
|-----------|-------------|
| AI Litigation Task Force | Created within DOJ (30-day deadline); coordinates federal defense of AI companies vs. state litigation |
| State Law Evaluation | Commerce Department must evaluate all US state AI laws within 90 days; identify conflicts with federal AI policy |
| FTC Policy Statement | FTC directed to issue AI deception and manipulation policy within 90 days |
| Preemption Intent | Federal government will challenge state AI laws that "obstruct" national AI policy |
| Exemptions | Explicitly exempts: child safety AI laws, AI compute infrastructure regulations, state AI procurement policies |

**Source:** [White House December 11, 2025 EO](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/), [Buchanan Ingersoll Analysis](https://www.bipc.com/new-executive-order-signals-federal-preemption-strategy-for-state-laws-on-artificial-intelligence)

---

### 5.3 Federal Agency AI Activities

| Agency | Key Action |
|--------|-----------|
| NIST | Published AI RMF 1.0 (Jan 2023), AI RMF 2.0 (Feb 2024), AI 600-1 GenAI Profile (Jul 2024); operates US AI Safety Institute |
| FTC | Section 5 enforcement against deceptive/unfair AI; directed by Dec 2025 EO to issue AI policy statement |
| DoD | DoD AI Strategy (updated 2023); Responsible AI principles; AI Assurance Office; Directive 3000.09 on autonomous weapons |
| CFPB | Circular 2023-03: AI in credit underwriting must comply with Equal Credit Opportunity Act |
| OCC/Fed Reserve | Interagency guidance applying SR 11-7 model risk management to AI/ML models |

---

## 6. What Are US State AI Laws?

By early 2026, over **40 states** had enacted or introduced AI-related legislation, creating a complex multi-jurisdictional compliance environment. The Trump December 2025 EO signaled intent to preempt conflicting state laws, but legal challenges are expected.

**Source:** [NCSL AI Legislation Tracker](https://www.ncsl.org/technology-and-communication/artificial-intelligence-2024-legislation)

### Key Enacted State Laws

| State | Law | Effective Date | Key Requirement |
|-------|-----|----------------|-----------------|
| **Colorado** | SB 205 — Artificial Intelligence Act | **February 1, 2026** | High-risk AI; impact assessments; anti-discrimination; consumer notice; developer and deployer obligations |
| **California** | AB 2013 — AI Training Data Transparency | January 1, 2026 | Disclosure of AI training data used in systems |
| **California** | AB 1008 — Personal Information in AI | January 1, 2026 | AI-processed personal data is covered by CCPA |
| **California** | SB 1047 — Frontier AI Safety | **Vetoed** Sept 2024 | Would have required safety testing for large models |
| **Illinois** | HB 3773 — AI Video Interview Act | January 1, 2020 | Employers must disclose AI use in video interviews; consent required |
| **Illinois** | SB 2781 — Insurance AI Fairness | 2024 | Prohibits AI-enabled insurance discrimination |
| **Texas** | SB 2 — TRAIGA | 2025 | High-risk AI obligations for developers and deployers |
| **New York City** | Local Law 144 | July 5, 2023 | Bias audits required for automated employment decision tools; results must be public |
| **Virginia** | HB 2481 — High-Risk AI Act | 2025 | High-risk AI in consequential decisions; impact assessments |
| **Utah** | HB 317 — AI Policy Act | March 13, 2024 | Disclosure of AI use in regulated industries |

**Sources:** [NCSL AI Legislation Database](https://www.ncsl.org/technology-and-communication/artificial-intelligence-2024-legislation), [Future of Privacy Forum State AI Law Tracker](https://fpf.org/blog/state-ai-legislation-tracker/)

---

### Colorado AI Act (SB 205) — Deepest State AI Law

**Effective:** February 1, 2026 (most comprehensive US state AI law; modeled on EU AI Act)

**Scope:** "High-risk AI systems" used in "consequential decisions" affecting:
- Employment / employment opportunities
- Education
- Financial / lending services
- Essential government services
- Healthcare
- Housing
- Insurance
- Legal services

**Developer Obligations:**
- Disclose intended use cases and known limitations to deployers
- Provide information about training data and performance metrics
- Maintain documentation to demonstrate compliance
- Use reasonable care to protect consumers from algorithmic discrimination

**Deployer Obligations:**
- Implement a risk management program governing AI use
- Complete impact assessment before deploying high-risk AI
- Notify consumers when high-risk AI is used in consequential decisions
- Allow consumers to appeal AI-assisted decisions
- Avoid algorithmic discrimination; "reasonable care" standard

**Enforcement:** Colorado AG has exclusive enforcement authority; no private right of action

**Source:** [Colorado SB 205 Text](https://leg.colorado.gov/bills/sb24-205)

---

## 7. What Are China's AI Regulations?

### 7.1 Regulatory Approach

China has adopted a **sequential, technology-specific approach** to AI regulation, targeting specific AI capabilities as they emerge. The primary regulator is the **Cyberspace Administration of China (CAC)**, coordinating with MIIT, MPS, and NDRC.

China's approach is notably more prescriptive than Western frameworks — requiring government approval **before** public release, mandatory registration, and content alignment with state ideology.

**Sources:** [Pertama Partners China AI Regulations](https://www.pertamapartners.com/insights/china-ai-regulations), [MMLC Group China AI Regulations](https://mmlcgroup.com/china-ai-regulations/)

---

### 7.2 Key Regulations (Chronological)

| Regulation | Effective | Regulator | Key Requirements |
|-----------|---------|---------|-----------------|
| **Algorithm Recommendation** | March 1, 2022 | CAC, MIIT, MPS, SAMR | Transparency; opt-out mechanism; no opinion manipulation; label AI content; major platforms register algorithms with CAC |
| **Deep Synthesis** | January 10, 2023 | CAC | Real-name verification; mandatory labeling of synthetic content; security assessments; prohibited uses (non-consensual imagery, impersonation) |
| **Generative AI Measures** | August 15, 2023 | CAC + 5 agencies | Pre-launch security assessment/filing (6–12+ months); socialist values content compliance; real-name verification; content logging for 6 months; data localization |

**Source:** [CAC Generative AI Measures Text](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm), [Pertama Partners Analysis](https://www.pertamapartners.com/insights/china-ai-regulations)

---

### 7.3 China Generative AI Measures — Key Requirements in Detail

**Pre-Launch Requirements:**
- Security assessment (备案 — CAC filing) before public launch
- Use legally sourced, authorized training data
- Training data must not violate national security, public interest, or individual rights
- Algorithm filing with CAC
- Timeline: typically 6–12+ months for complex models

**Operational Requirements:**
- Content must align with "社会主义核心价値观" (socialist core values)
- Content must not subvert state power, undermine social stability, or promote terrorism
- Implement real-name verification for users
- Publish service rules and content moderation mechanisms
- Label all AI-generated content
- Maintain logs of inputs and outputs for at least 6 months

**Data Requirements:**
- Data localization: data collected in China must be stored in China
- Cross-border data transfers require separate approval
- Personal information processing must comply with Personal Information Protection Law (PIPL)

**Foreign Service Compliance:**
- Foreign services accessible in China are subject to compliance if they serve Chinese users
- Government retains authority to demand algorithm modifications at any time

**Source:** [CAC Generative AI Measures Text](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)

---

### 7.4 China vs. Western AI Regulation

| Feature | China | EU AI Act | US Federal |
|---------|-------|-----------|------------|
| Pre-launch approval required | Yes (mandatory filing) | No (post-market surveillance) | No |
| Ideological content requirements | Yes (socialist core values) | No | No |
| Real-name verification | Mandatory | Not required | Not required |
| Data localization | Yes | No (GDPR-compliant transfers allowed) | No federal law |
| Government algorithm modification rights | Yes | No | No |
| Penalties | Service suspension, fines, criminal | €35M / 7% revenue | Varies (FTC: $50K/day) |
| Foreign service compliance | Yes (if Chinese users) | Yes (if EU market) | No (US-centric) |

---

## 8. What Are Industry-Specific AI Regulations?

### 8.1 Financial Services

#### SR 11-7: Model Risk Management (US Banking)

| Detail | Value |
|--------|-------|
| Issued by | Federal Reserve Board + OCC |
| Date | April 2011 (foundational; still applicable) |
| Applicability | US banks, savings associations, bank holding companies |
| AI/ML Relevance | Applied to AI/ML models in credit underwriting, fraud detection, AML, stress testing |

**Key Requirements:**
- Independent model validation before deployment
- Ongoing model monitoring and periodic revalidation
- Documented conceptual soundness
- Model inventory managed by independent model risk function
- Tiered model risk rating (low/medium/high)
- Board and senior management oversight

**Source:** [Federal Reserve SR 11-7 Letter](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm)

---

#### SS1/23: Model Risk Management (UK Banking)

| Detail | Value |
|--------|-------|
| Issued by | Bank of England Prudential Regulation Authority (PRA) |
| Date | May 2023 |
| Applicability | UK PRA-regulated banks and insurance companies |

**Key Updates vs. SR 11-7:**
- Explicitly addresses AI/ML complexity and opacity
- Board-level model risk appetite requirement
- Third-party/vendor model risk coverage
- Model lifecycle coverage including decommissioning

**Source:** [Bank of England SS1/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks)

---

#### DORA: Digital Operational Resilience Act (EU Financial Services)

| Detail | Value |
|--------|-------|
| Effective | January 17, 2025 |
| Applicability | Banks, insurers, investment firms, payment institutions, crypto-asset service providers in EU |
| AI Relevance | AI systems qualifying as "ICT systems" are subject to DORA |

**Key AI-Relevant Requirements:**
- ICT (AI) risk management framework required
- ICT-related incident reporting: significant incidents within 4 hours initial; final report within 1 month
- Third-party ICT provider risk management — AI vendors are subject to oversight and contractual requirements
- Threat-led penetration testing (TLPT) for designated entities
- ICT concentration risk assessment for single-provider dependency

**Source:** [EBA DORA Guidance](https://www.eba.europa.eu/regulation-and-policy/operational-resilience/digital-operational-resilience-act-dora)

---

#### GDPR Article 22: Automated Decision-Making

**Effective:** May 25, 2018 (EU-wide)

**Scope:** Automated processing of personal data to make decisions with significant legal or similarly significant effects on individuals

**Key Provisions:**
- Right not to be subject to solely automated decisions affecting legal status
- Exceptions: consent, contractual necessity, EU/Member State law (with safeguards)
- When exceptions apply: right to human review; right to contest; right to explanation

**AI Compliance Implications:**
- AI credit scoring, insurance pricing, hiring, benefits — all implicated
- "Meaningful explanation" creates de facto explainability obligation
- DPIA required for systematic automated processing
- EU AI Act high-risk provisions layer on top

**Source:** [GDPR Article 22 Text](https://gdpr-info.eu/art-22-gdpr/), [ICO Automated Decision-Making Guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/automated-decision-making-and-profiling/)

---

### 8.2 Healthcare

#### FDA AI/ML-Based Software as a Medical Device (SaMD)

**Key Guidance Documents:**
- "AI/ML-Based SaMD Action Plan" (January 2021) — Framework for adaptive AI
- "Marketing Submission Recommendations for AI/ML-Based SaMD" (October 2023) — 510(k)/PMA requirements for AI
- "Good Machine Learning Practice (GMLP)" (October 2021) — Joint with Health Canada and UK MHRA

**Key Requirements:**
- Predetermined change control plan (PCCP) for adaptive/continuously learning AI
- Total Product Lifecycle (TPLC) approach from design through post-market monitoring
- Real-world performance monitoring post-market
- Transparency to users about AI capabilities, limitations, and intended use
- Independent performance testing on clinically meaningful populations

**Source:** [FDA AI/ML Action Plan](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device)

---

#### HIPAA and Healthcare AI

**AI-Specific HIPAA Risk Areas:**
- LLMs trained on clinical notes may memorize and reproduce ePHI
- AI inference about health conditions from non-health data may create de facto ePHI
- Third-party AI APIs — Business Associate Agreement (BAA) enforceability

**Key Requirements:**
- Access controls governing who can query AI models trained on ePHI
- Audit controls logging AI system access to ePHI
- Minimum necessary standard: AI accesses only ePHI necessary for its function
- BAAs required with all AI vendors processing ePHI

**Source:** [HHS HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html), [OCR AI and HIPAA Guidance](https://www.hhs.gov/sites/default/files/ai-and-hipaa-bulletin.pdf)

---

## 9. How Do Global AI Regulations Compare?

### Comprehensive Regulatory Comparison Matrix

| Regulation | Jurisdiction | Enforcer | Max AI Penalty | Key AI Obligation | Type |
|------------|-------------|----------|----------------|-------------------|------|
| **EU AI Act** | EU/EEA | National MSAs + EU AI Office | €35M / 7% revenue | Risk assessment; human oversight; CE marking | Hard law |
| **GDPR Art. 22** | EU/EEA | Data Protection Authorities | €20M / 4% revenue | Right to explanation; human review of automated decisions | Hard law |
| **DORA** | EU financial | ECB, EBA, ESMA, NCAs | €10M / 2% revenue | ICT risk management; 3rd-party oversight; incident reporting | Hard law |
| **Colorado SB 205** | Colorado, US | Colorado AG | Injunctive relief; civil penalties | Impact assessment; anti-discrimination; consumer notice | State law |
| **NYC Local Law 144** | New York City | NYC DCA | $500–$1,500/violation | Annual bias audit; public results disclosure | City law |
| **SR 11-7** | US federal banking | OCC, Fed Reserve | Supervisory action | Model validation; independent review; monitoring | Guidance |
| **SS1/23** | UK banking | PRA | Supervisory action | Model risk appetite; lifecycle governance; 3rd-party | Guidance |
| **HIPAA Security Rule** | US healthcare | HHS OCR | $100–$1.9M/category | Access controls; audit logs; BAAs with AI vendors | Federal law |
| **FDA SaMD** | US medical devices | FDA | Recall; civil monetary penalties | PCCP; TPLC; performance testing; post-market monitoring | Federal regulation |
| **China GenAI Measures** | China | CAC | Service suspension; fines; criminal | Security filing; socialist values; real-name verification | Hard law |

---

### Regulatory Approach Comparison

| Dimension | EU AI Act | US (Federal) | US (States) | China | UK |
|-----------|-----------|--------------|-------------|-------|-----|
| **Regulatory model** | Horizontal regulation | Sector-specific + guidance | Horizontal (emerging) | Technology-specific | Principles-based |
| **Binding** | Yes (hard law) | Partial (EOs; FTC enforcement) | Yes (enacted laws) | Yes (hard law) | Guidance (for now) |
| **Pre-market approval** | High-risk conformity assessment | FDA for medical only | Some registration | Mandatory filing for GenAI | No |
| **Penalties** | High (7% revenue) | Moderate (sector-specific) | Varies by state | Severe (suspension + criminal) | Lower (currently) |
| **Ideological requirements** | No | No | No | Yes (socialist values) | No |
| **Risk-based approach** | Yes (4 tiers) | Mostly | Yes (Colorado, Virginia) | Mostly | Yes |
| **Extraterritorial reach** | Yes (EU market access) | Limited | State-level | Yes (if Chinese users) | Limited (for now) |

---

## 10. What Is the Global AI Regulatory Timeline?

```
2018:
  GDPR Article 22 becomes operative (automated decision-making rights)

2020:
  Illinois AI Video Interview Act (disclosure of AI in hiring)

2021:
  SR 11-7 increasingly applied to AI/ML models by US banking regulators
  China: MIIT issues AI development guidance
  Biden: AI Initiative National Security Memorandum

2022:
  China: Algorithm Recommendation Regulations (Mar 1)
  US: NIST initiates AI RMF development
  EU AI Act: European Parliament committee approval process

2023:
  China: Deep Synthesis (Deepfake) Regulations (Jan 10)
  NIST AI RMF 1.0 published (Jan 26)
  ISO/IEC 23894 AI Risk Management Guidance (Feb)
  ISO/IEC 42001 AI Management Systems Standard (Dec 18 — published)
  China: Generative AI Measures (Aug 15)
  Biden: Executive Order 14110 AI Safety (Oct 30)
  NYC: Local Law 144 Bias Audits (Jul 5)
  EU AI Act: Political agreement reached (Dec)

2024:
  EU AI Act: Published in Official Journal; enters into force (Aug 2)
  NIST AI RMF 2.0 published (Feb)
  NIST AI 600-1 GenAI Profile published (Jul 26)
  DORA: Digital Operational Resilience Act effective (Jan 17)
  ISO/IEC 42001 widely available for certification (2024)
  Colorado SB 205 enacted (May)
  California SB 1047 vetoed by Gov. Newsom (Sept)

2025:
  EU: Prohibited AI systems ban effective (Feb 2)
  Trump: Rescinds Biden EO 14110 (Jan 20)
  EU: GPAI model obligations for new systems (Aug 2)
  Bank of England SS1/23: Increasingly applied to AI models
  UK AI Opportunities Action Plan (Jan)
  Trump: Federal preemption EO on state AI laws (Dec 11)

2026:
  Colorado SB 205 effective (Feb 1) ← NOW ACTIVE
  EU: High-risk AI operator compliance (Aug 2)
  Texas TRAIGA effective
  Virginia HB 2481 effective
  California AB 2013, AB 1008 effective (Jan 1)

2027:
  EU: Full compliance for existing GPAI models (Aug 2)
  EU: High-risk AI in regulated products (Aug 2)
  Gartner: AI TRiSM-as-a-Service expected to emerge

2030:
  EU: Large-scale IT system AI compliance (Dec 31)
  Gartner: AI TRiSM expected to reach mainstream adoption
```

---

*For vendor tools that support specific regulatory frameworks, see [platform-comparison.md](platform-comparison.md). For implementation guidance, see [implementation-guide.md](implementation-guide.md).*

*Sources: [EU AI Act Official Text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689), [artificialintelligenceact.eu](https://artificialintelligenceact.eu), [DataGuard EU AI Act Timeline](https://www.dataguard.com/eu-ai-act/timeline), [ModelOp EU AI Act](https://www.modelop.com/ai-governance/ai-regulations-standards/eu-ai-act), [White House December 2025 EO](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/), [Buchanan Ingersoll](https://www.bipc.com/new-executive-order-signals-federal-preemption-strategy-for-state-laws-on-artificial-intelligence), [NIST AI RMF](https://airc.nist.gov/Home), [Reed Smith NIST AI 600-1](https://www.reedsmith.com/articles/managing-genai-takeaways-nist-guidance-responsible-genai-implementation/), [ISO/IEC 42001](https://www.iso.org/standard/81230.html), [Pertama Partners China AI Regs](https://www.pertamapartners.com/insights/china-ai-regulations), [Federal Reserve SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm), [NCSL AI Legislation](https://www.ncsl.org/technology-and-communication/artificial-intelligence-2024-legislation)*

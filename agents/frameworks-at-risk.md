# Agent Frameworks at Risk

> Security risk assessment of major AI agent frameworks. Covers known vulnerabilities, attack surfaces, and risk ratings based on architecture patterns.

**Last updated:** March 2026

---

## Framework Risk Matrix

| Framework | Maintainer | GitHub Stars | License | Agent Type | Risk Rating | Key Vulnerabilities |
|-----------|-----------|-------------|---------|------------|:-----------:|--------------------|
| **LangChain** | LangChain Inc | 98k+ | MIT | General-purpose orchestration | HIGH | Arbitrary code execution via Python REPL tool; prompt injection in retrieval chains; unrestricted file system access via default tools |
| **LangGraph** | LangChain Inc | 8k+ | MIT | Stateful multi-agent | HIGH | State manipulation across graph nodes; cyclic execution loops; shared memory poisoning between agents |
| **CrewAI** | CrewAI Inc | 25k+ | MIT | Role-based multi-agent | MEDIUM-HIGH | Inter-agent trust assumed by default; no message signing between crew members; delegation chains can escalate privileges |
| **AutoGen** | Microsoft | 38k+ | MIT | Conversational multi-agent | MEDIUM-HIGH | Code execution enabled by default in some configs; agents can install packages; group chat context shared without access controls |
| **OpenAI Agents SDK** | OpenAI | 15k+ | MIT | Tool-calling agents | MEDIUM | Tool call parameter injection; handoff trust assumptions; guardrail bypass via multi-step reasoning |
| **AWS Bedrock Agents** | Amazon | N/A (managed) | Proprietary | Enterprise managed agents | MEDIUM | Action group over-permissioning; knowledge base poisoning via S3; Lambda function injection |
| **Semantic Kernel** | Microsoft | 22k+ | MIT | Enterprise AI orchestration | MEDIUM | Plugin trust assumptions; planner manipulation via prompt injection; memory store poisoning |
| **Replit Agent** | Replit | N/A (SaaS) | Proprietary | Code generation agent | HIGH | Unrestricted code execution in workspace; vibe coding runaway (OWASP-cited); file system access without sandboxing |
| **Devin** | Cognition AI | N/A (SaaS) | Proprietary | Autonomous coding agent | HIGH | Full development environment access; git commit capability; production deployment actions |
| **GitHub Copilot Workspaces** | GitHub/Microsoft | N/A (SaaS) | Proprietary | Code agent | MEDIUM-HIGH | Code repository access; PR creation; indirect injection via code comments (cited in AgentFlayer) |
| **Salesforce Agentforce** | Salesforce | N/A (SaaS) | Proprietary | CRM agent platform | MEDIUM-HIGH | Customer data access; AgentFlayer vulnerability (Zenity Labs Aug 2025); action execution on CRM records |
| **Microsoft 365 Copilot** | Microsoft | N/A (SaaS) | Proprietary | Enterprise productivity agent | HIGH | EchoLeak zero-click exploit (OWASP-cited); email/calendar/document access; indirect injection via meeting invites |

---

## Risk Rating Criteria

| Rating | Definition |
|--------|------------|
| **HIGH** | Framework enables autonomous code execution, file system access, or external communications with minimal guardrails by default |
| **MEDIUM-HIGH** | Framework enables tool use and multi-agent coordination with some guardrails but known bypass patterns |
| **MEDIUM** | Framework has security controls but known attack vectors exist in specific configurations |
| **LOW** | Framework has strong default security posture with limited autonomous action capability |

---

## Common Vulnerability Patterns

### 1. Default-Unsafe Configurations
Many frameworks ship with powerful tools enabled by default (Python REPL, file system, shell access). Developers who follow quickstart guides deploy agents with maximum attack surface.

**Affected:** LangChain, AutoGen, Replit Agent

### 2. Inter-Agent Trust Assumptions
Multi-agent frameworks assume all agents in a workflow are trustworthy. No message authentication, no semantic validation, no privilege boundaries between agents.

**Affected:** CrewAI, LangGraph, AutoGen, Salesforce Agentforce

### 3. Memory/Context Shared Without Access Controls
Agent memory stores (short-term context, long-term RAG) are accessible to all agents in a system without read/write permissions.

**Affected:** LangGraph, CrewAI, Semantic Kernel, AutoGen

### 4. Indirect Prompt Injection in Retrieved Content
All frameworks that perform RAG or tool-based data retrieval are vulnerable to indirect prompt injection in the retrieved content.

**Affected:** All frameworks listed above

---

## Mitigation Recommendations by Framework

| Framework | Priority Mitigation |
|-----------|--------------------|
| LangChain | Disable Python REPL and shell tools in production; use LangSmith for execution tracing |
| LangGraph | Implement state validation between nodes; add circuit breakers for cyclic graphs |
| CrewAI | Add message signing between agents; implement role-based tool access per crew member |
| AutoGen | Disable auto code execution; use Docker sandboxing; restrict package installation |
| OpenAI Agents SDK | Validate all tool call parameters; implement guardrail functions; audit handoff chains |
| Replit Agent | Restrict file system scope; require human approval for package installs and deploys |

---

## Sources

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Zenity Labs AgentFlayer Research (Aug 2025)](https://zenity.io/blog/current-events/zenity-named-a-2025-cool-vendor-in-gartner-s-agentic-ai-trism-report)
- [CSA Agentic AI Predictions 2026](https://cloudsecurityalliance.org/blog/2026/01/16/my-top-10-predictions-for-agentic-ai-in-2026)
- [SecurityLab-UCD AI Agent Security Paper](https://github.com/SecurityLab-UCD/ai-agent-security)

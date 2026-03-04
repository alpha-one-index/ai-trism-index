# Model Context Protocol (MCP) Security

> Analysis of supply chain risks, malicious server incidents, and authentication patterns for the Model Context Protocol — the emerging standard for connecting AI agents to external tools and data sources.

**Last updated:** March 2026

---

## What Is MCP?

The Model Context Protocol (MCP), introduced by Anthropic in late 2024, is an open standard for connecting AI agents to external tools, data sources, and services. It provides a standardized interface for agents to discover and invoke tools, replacing ad-hoc API integrations.

**Adoption:** MCP has been adopted by major agent frameworks including LangChain, OpenAI Agents SDK, AWS Bedrock, and Cursor AI. It is rapidly becoming the default integration layer for enterprise AI agents.

---

## OWASP Risk Alignment

MCP security maps directly to multiple OWASP Agentic Top 10 risks:

| OWASP Risk | MCP Relevance |
|-----------|---------------|
| R4: Agentic Supply Chain Vulnerabilities | Malicious MCP servers, poisoned tool registries |
| R7: Insecure Inter-Agent Communication | Unauthenticated MCP connections, message tampering |
| R3: Identity & Privilege Abuse | MCP servers inheriting agent/user credentials |
| R1: Agent Goal Hijacking | Malicious MCP servers returning crafted responses with injection payloads |

---

## Known MCP Security Incidents

### 1. Malicious Postmark MCP Server (npm)

**Date:** Early 2026
**Source:** OWASP Top 10 for Agentic Applications 2026

The first documented in-the-wild malicious MCP server was published to npm impersonating the legitimate Postmark email service. When agents connected to it, the server secretly BCC'd all outgoing emails to an attacker-controlled address.

**Impact:** Data exfiltration via email forwarding without user or agent awareness.

### 2. MCP Server Impersonation via Spoofed Descriptors

**Date:** 2025-2026
**Source:** OWASP Top 10 for Agentic Applications 2026

A malicious MCP endpoint advertised spoofed agent descriptors and fake capabilities. When trusted by an orchestrating agent, it routed sensitive data through attacker infrastructure while appearing to provide legitimate tool functionality.

**Impact:** Man-in-the-middle data interception in multi-agent workflows.

---

## MCP Attack Surface

| Attack Vector | Description | Severity |
|--------------|-------------|:--------:|
| **Registry Poisoning** | Publishing malicious MCP servers to npm/PyPI with names similar to legitimate packages | HIGH |
| **Descriptor Spoofing** | MCP server returns false capability descriptions to manipulate agent tool selection | HIGH |
| **Response Injection** | MCP server returns tool results containing prompt injection payloads | CRITICAL |
| **Credential Theft** | MCP server captures OAuth tokens or API keys passed by agents during authentication | CRITICAL |
| **Dependency Hijacking** | Compromising dependencies of legitimate MCP servers | HIGH |
| **Version Rollback** | Serving older, vulnerable versions of MCP server implementations | MEDIUM |
| **Tool Shadowing** | Registering MCP tools with names that override legitimate tools | HIGH |

---

## MCP Authentication Patterns

### Current State (Mostly Unauthenticated)

Most MCP connections today lack standardized authentication. Agents connect to MCP servers based on configuration, with trust established by the deploying developer rather than verified at runtime.

### Recommended Authentication Patterns

| Pattern | Description | Maturity |
|---------|-------------|:--------:|
| **mTLS** | Mutual TLS between agent and MCP server; both parties verify certificates | Production-ready |
| **OAuth 2.0 Scoped Tokens** | Agent presents scoped OAuth token; MCP server validates and enforces scopes | Emerging |
| **Server Signing** | MCP server signs responses; agent verifies signature before processing | Proposed |
| **Registry Verification** | MCP servers verified against a trusted registry with cryptographic attestation | Early design |
| **SBOM for MCP** | Software bill of materials for MCP server dependencies | Proposed |

### Defense-in-Depth for MCP

1. **Allow-list MCP servers** — Only connect to pre-approved, verified MCP servers
2. **Verify server identity** — Use mTLS or signed server certificates
3. **Inspect responses** — Scan MCP tool responses for prompt injection patterns before feeding to agent
4. **Scope credentials** — Never pass broad credentials to MCP servers; use minimum-scope tokens
5. **Monitor tool calls** — Log all MCP interactions for audit and anomaly detection
6. **Pin versions** — Lock MCP server versions; review updates before deployment

---

## Mitigating Vendors

| Vendor | MCP Security Capability |
|--------|------------------------|
| **Gravitee** | MCP gateway with server authentication, rate limiting, and request/response inspection |
| **ProtectAI** | Supply chain scanning for MCP server dependencies |
| **Snyk** | Dependency vulnerability scanning for MCP packages |
| **Zenity** | Runtime monitoring of MCP tool calls within agent execution chains |
| **Pangea** | Security APIs for MCP authentication and audit logging |

---

## Sources

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Gravitee MCP Gateway Blog](https://www.gravitee.io/blog/owasp-top-10-for-agentic-applications-2026-a-practical-review)
- [Anthropic MCP Specification](https://modelcontextprotocol.io/)
- [Palo Alto OWASP Agentic Analysis](https://www.paloaltonetworks.com/blog/cloud-security/owasp-agentic-ai-security/)

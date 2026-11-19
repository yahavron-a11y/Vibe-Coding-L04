# Architect Expansion Complete — `sec_architecture.tex` (10+ Pages Hebrew LuaLaTeX PDR)

## Updated File Paths
- Expanded Hebrew LaTeX Sections (updated in-place):
  `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\L04\agents\architect\sec_architecture.tex`
- LuaLaTeX BiDi Hebrew Document Class (unchanged, 100% compatible):
  `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\L04\agents\architect\pdr_hebrew.cls`

## Summary of Expanded Content in `sec_architecture.tex`
1. **Section 1: 5-Layer System Architecture (`\label{sec:5layer-arch}`)**
   - Core architectural principles (Operational Determinism, Async Queue-Based Messaging, Workspace Sandboxing, Native BiDi UTF-8 Pipeline).
   - Detailed component specifications for all 5 layers (Layer 5 Presentation/CLI/Governance, Layer 4 Multi-Agent Hub & Orchestration, Layer 3 Specialized Agents & Cognitive Processing, Layer 2 Tooling/Execution/Sandbox, Layer 1 Persistence/State/Observability).
   - **TikZ Diagram 1 (`fig:5layer-arch`)**: 5-Layer Architecture with Cross-Cutting Security/Audit/Telemetry Bus (wrapped in `ltrtikz`).
   - **TikZ Diagram 2 (`fig:deployment-topo`)**: Windows Local Host Multi-Process Deployment & Runtime Topology with MiKTeX/LuaLaTeX compiler (wrapped in `ltrtikz`).
2. **Section 2: Multi-Agent Hub Protocol, Schemas & API Contracts (`\label{sec:hub-spec}`)**
   - Message Envelope Schema table (`id`, `kind`, `from`, `to`, `timestamp`, `payload`, `ttl_sec`).
   - Complete CLI/IPC API Contracts `longtable` (`join`, `wait`, `reply`, `ping-all`, `todo-claim`, `todo-done`).
   - **TikZ Diagram 3 (`fig:hub-topology`)**: Multi-Agent Hub Topology & Shared TODO Board (wrapped in `ltrtikz`).
   - **TikZ Diagram 4 (`fig:hub-sequence`)**: End-to-End Sequence Diagram (`Master -> Hub -> Architect -> TODO Board -> Reply`, wrapped in `ltrtikz`).
   - **TikZ Diagram 5 (`fig:agent-fsm`)**: Agent Listen-Loop State Machine (`BOOT/JOIN -> LISTENING -> EXECUTING -> REPLYING / ERROR`, wrapped in `ltrtikz`).
3. **Section 3: Data Models & Persistence Architecture (`\label{sec:data-models}`)**
   - Logical Data Model table (`AgentSession`, `MessageRecord`, `TodoItem`, `ArtifactFile`, `AuditEvent`) + UTF-8 BiDi storage guarantees `archbox`.
4. **Section 4: Comprehensive Functional Requirements (`\label{sec:fr-spec}`)**
   - Full `longtable` covering **FR-01 through FR-20** with category, acceptance criteria, MoSCoW priority, and verification method.
5. **Section 5: Comprehensive Non-Functional Requirements (`\label{sec:nfr-spec}`)**
   - Full `longtable` covering **NFR-01 through NFR-15** with quantitative SLAs/metrics, verification methods, and priorities.
6. **Section 6: Failure Modes, FMEA & Recovery (`\label{sec:fmea-recovery}`)**
   - Full FMEA `longtable` covering agent crash, `todo-claim` race condition, hub crash, UTF-8/BiDi corruption, LuaLaTeX compile failure, and message storms, with root causes, detection, mitigation, and RTO targets.
7. **Section 7: Security, Isolation & Governance Architecture (`\label{sec:security-arch}`)**
   - Threat model, process/network isolation, identity & reply integrity, auditability/compliance, and PDR readiness summary `archbox`.

All tables use `longtable` or `tabularx` for clean multi-page pagination, and all 5 TikZ diagrams are wrapped in `ltrtikz` for full LuaLaTeX BiDi compatibility with `pdr_hebrew.cls`.

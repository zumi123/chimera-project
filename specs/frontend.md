# Frontend Specification — Project Chimera

Purpose
-------
Provide a lightweight UI for humans and operators to inspect agent activity, approve high-risk actions, and observe telemetry and trace data. The UI focuses on transparency and governance rather than authoring agents.

Target Users
------------
- Operator / Moderator: reviews content and approves publishing
- Developer / Orchestrator: inspects specs, tests, and agent runs
- Auditor: views telemetry, run traces, and decision logs

Primary Screens
---------------
1) Dashboard (Home)
   - Purpose: High-level service health and recent agent runs.
   - Elements: Summary cards (agents online, failing runs, pending approvals), recent run table (timestamp, agent_id, spec_ref, status), search bar.

2) Run Inspector
   - Purpose: Inspect single agent run and decide action.
   - Elements: Run header (run_id, agent_id, start_time, spec_version), trace log (structured steps), input/output JSON (with schema validation status), attachments (assets, thumbnails), Approve / Reject buttons with reason box.
   - Acceptance: Approve must create a signed approval record in DB with a link to the PR or action taken.

3) Specs Browser
   - Purpose: Read & compare specs.
   - Elements: File tree for `specs/`, JSON schema viewer with validation examples, spec history and `spec_version` metadata.

4) Skills Catalog
   - Purpose: List available runtime skills and their I/O contracts.
   - Elements: Skill name, version, input schema preview, output schema preview, last-run status, docs link.

5) Governance / Audit
   - Purpose: Search and filter telemetry and MCP Sense logs.
   - Elements: Filters (agent_id, spec_ref, run_id, time range), export CSV, link to raw telemetry.

User Flows
----------
Flow A — Inspect and Approve a Run
- Operator navigates to Dashboard → clicks a failing or pending run → Run Inspector opens → reviews input/output and trace → clicks `Approve` with a short reason → system records approval (signed) and triggers downstream action (publish or continue workflow).

Flow B — Add / View Spec
- Developer opens Specs Browser → selects `specs/technical.md` → compares latest `spec_version` with implementation → optionally opens issue to request spec change.

Flow C — Review Skill Contract
- Operator opens Skills Catalog → selects `skill_transcribe_audio` → views input/output schemas and sample payloads → runs a test invocation (sandboxed) to preview output.

Wireframes & Acceptance
-----------------------
- All screens must show `spec_version` where relevant.
- Actions that change system state must record `run_id` and `actor` with timestamp.
- Approval actions require at least one human reviewer.

Security & Auth
---------------
- SSO (OAuth) for users; roles: `operator`, `developer`, `auditor`.
- Approvals require `operator` role.

Implementation Notes
--------------------
- Frontend: React + Typescript, small component library.
- Backend: lightweight API that proxies reads from DB and MCP Sense, ensures schema validation is performed server-side.

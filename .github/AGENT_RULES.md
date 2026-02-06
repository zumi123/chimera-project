# Project Chimera — Agent Rules (Human-Readable)

Purpose
-------
This document summarises the governance rules agents and developer-facing tools must follow when operating in the Project Chimera repository. It is a human-visible version of `.cursor/rules` designed for reviewers, CI, and contributors.

Prime Directive
---------------
1. Never create or modify implementation code without citing the authoritative spec section in `specs/` that permits the change. Every proposed change must include a `spec_ref` (path + section) in the commit message or PR description.
2. All runtime input and output must conform to JSON Schemas stored in `specs/schemas/`.
3. All non-trivial changes must be accompanied by tests that express the intended behavior; prefer failing-tests-first (TDD).

Traceability and Telemetry
-------------------------
- Every automated run (agent or CI) must publish a `trace` object with fields: `spec_version`, `run_id` (UUID), `actor` (agent_id or username), and `spec_ref`.
- Telemetry events must be recorded to MCP Sense with `user`, `agent_id`, `spec_ref`, and `run_id`.

Behavior Rules for Agents
-------------------------
- Plans before code: Before taking actions that modify files, agents must produce a brief plan (3–6 steps) that references the relevant `spec_ref`.
- Explain rationale: Agents must include a one-line justification for each modification.
- Fail fast & safe: If uncertain about safety, agents must stop and escalate to human review.
- Minimum permissions: Agents should run with least privilege for file system and network access.

PR and Review Requirements
--------------------------
- PR title must include `spec_ref: <path>` if code changes implement a spec.
- PR description must contain: summary, spec references, tests added, and how the change preserves safety.
- The CI must pass, including spec checks and tests, before merging.

Security and Key Management
---------------------------
- Messages published to external networks (OpenClaw etc.) must be signed. Agent onboarding must include public key registration in the MCP registry.

Contributing & Exceptions
-------------------------
- For minor docs-only updates, cite the relevant spec and note `docs-only` in the PR body.
- Exception workflow: When a deviation is necessary, open an issue referencing the unsafe assumption and tag `governance/exception` for human approval.

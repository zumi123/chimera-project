# Project Chimera — Specs Meta

Vision
-------
Project Chimera is an agentic infrastructure that produces short-form social video content autonomously while adhering to explicit, auditable specifications. Specs are the single source of truth for agents and humans.

Constraints
-----------
- Agents MUST consult `specs/technical.md` before writing or modifying code.
- All runtime inputs/outputs must conform to declared JSON schemas in `specs/technical.md`.
- Changes must reference a spec section and pass CI checks before merging.

Scope
-----
This repo focuses on agent orchestration, skills interfaces, and governance (spec-driven development, traceability, and TDD).

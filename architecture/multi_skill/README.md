# Multi-Skill Architecture — Project Chimera

Overview
--------
This folder describes the multi-skill architecture: a Coordinator Agent orchestrates specialized Skill Agents. Skills are lightweight, versioned capabilities that expose stable I/O contracts.

Components
----------
- Coordinator Agent: Accepts high-level tasks, decomposes into skill invocations, aggregates results, enforces rate limits and approvals.
- Skill Agents: Small services (or function-style handlers) implementing a single capability (download, transcribe, compose, publish).
- Job Queue: Redis or message broker for dispatching skill jobs.
- Store: Postgres for canonical objects; object store (S3) for large assets.
- Telemetry: MCP Sense to record traces and decisions.

Best Practices
--------------
- Skills must be idempotent and report `trace` metadata.
- Version skills via `skill_name:version` and allow coexistence while migrating.
- Use JSON Schemas for all skill inputs/outputs stored in `specs/schemas/`.

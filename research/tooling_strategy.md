# Tooling & MCP Strategy

Developer MCPs (IDE-time tools)
-------------------------------
- `git-mcp`: Git operations mirrored to MCP for traceability and provenance.
- `filesystem-mcp`: Allows safe, auditable file edits by agents (with run_id and spec reference).
- `telemetry-mcp` (Tenx MCP Sense): Record agent decisions and plans for audit.

Runtime Skills vs Dev MCPs
--------------------------
- Dev MCPs help humans and dev-time agents author, test, and review code.
- Runtime Skills are packaged capabilities invoked by agents at runtime (e.g., `skill_download_youtube`).

Recommended Setup
-----------------
- Use Postgres for primary store and a lightweight message queue (Redis or RabbitMQ) for job dispatch.
- Configure MCP Sense telemetry to include `user`, `agent_id`, `spec_ref`, and `run_id` on all operations.

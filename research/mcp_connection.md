# MCP Sense Connection — Verification

This file documents the MCP Sense configuration and how to verify telemetry is being recorded.

Config
------
The project contains an MCP config at `.vscode/mcp.json` pointing to the Tenx MCP proxy.

To verify locally
-----------------
1. Ensure your IDE has the Tenx MCP extension enabled and is using the workspace settings.
2. Trigger an action (open a spec file and save, run a test) and confirm telemetry appears in your MCP dashboard.
3. Each telemetry entry should include `user`, `agent_id`, `spec_ref`, and `run_id`.

Note
----
We cannot programmatically verify remote MCP ingestion from this repo; this document is a checklist to confirm the connection during your session.

# OpenClaw / Agent Social Network Integration (concept)

Objective
---------
Provide a lightweight availability/status and capability announcement protocol so Chimera agents can interoperate with OpenClaw-style networks.

Publish Model
-------------
- `/status/publish` — announce availability
  - payload: { "agent_id": "uuid", "capabilities": ["skill:download","skill:transcribe"], "trust_level": "string", "endpoint": "url" }

- `/status/query` — query agent capabilities

Security
--------
- Sign messages with an agent keypair. Exchange public keys via the MCP registry when onboarding.

Social Protocols
----------------
- Heartbeats: agents must send periodic heartbeats with TTL.
- Backoff & Rate-limits: advertise `max_concurrent_jobs` and `rate_limit` fields.

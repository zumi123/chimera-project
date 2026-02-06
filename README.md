# Project Chimera — 3-Day Challenge

Project Chimera is a spec-first, test-first foundation for building autonomous influencer agents. The repository is organised to make specs the source of truth, enable agent runtime skills, and enforce governance through CI and telemetry.

What’s included
- `specs/` — high-level, functional, and technical specs (API contracts, DB schema, OpenClaw integration).
- `specs/schemas/` — JSON Schemas for API responses and skill interfaces.
- `skills/` — skill interface descriptions and runtime stubs (skill_download_video, skill_transcribe_audio, skill_compose_short_video).
- `tests/` — failing tests (TDD) that define the empty slots agents should implement.
- `research/` — architecture strategy, tooling strategy, and MCP connection notes.
- `.cursor/rules` — IDE agent rules and the Prime Directive (always reference specs first).
- `Dockerfile`, `Makefile` — reproducible test environment and helper commands.
- `.github/workflows/main.yml` — CI that runs `make test` on push.

Quickstart

- Install dev deps locally (recommended in a venv):

```bash
python3 -m pip install --upgrade pip
python3 -m pip install pytest jsonschema
```

- Run tests locally:

```bash
make test
# or
python3 -m pytest -q
```

- Run tests in Docker (isolated):

```bash
docker build -t chimera-project:test .
docker run --rm chimera-project:test
```

Notes on TDD and Day 3
- The `tests/` folder intentionally contains failing tests (Day 3 TDD artifacts). Implementations should satisfy the specs in `specs/` and update tests only after a spec-verified implementation exists.

MCP / Telemetry
- `.vscode/mcp.json` configures the workspace MCP Sense connection. See `research/mcp_connection.md` for verification steps.

Contributing
- Follow the Prime Directive in `.cursor/rules`: always reference specs before writing code.
- Commit messages should reference the spec path (e.g., "Implement: specs/technical.md#TrendFetcher").

Contact / Submission
- For the 3-day challenge deliverables, ensure the repo contains `specs/`, `tests/`, `skills/`, `Dockerfile`, `Makefile`, `.github/workflows/`, and `.cursor/rules`. Include a Loom video and MCP Sense telemetry as required by the challenge.


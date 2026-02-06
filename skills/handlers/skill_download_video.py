import uuid
from typing import Dict


def handle(input: Dict) -> Dict:
    """Download video skill handler (stub).

    Input contract (example):
    {
      "source_url": "string",
      "max_duration_seconds": int (optional)
    }

    Output must follow `specs/schemas/skill_download_video.schema.json`.
    """
    run_id = str(uuid.uuid4())
    # Minimal behavior: return OK response and include trace
    return {
        "status": "ok",
        "asset_path": "/tmp/example_video.mp4",
        "duration_seconds": 30,
        "metadata": {"source_url": input.get("source_url")},
        "trace": {"spec_version": "0.1", "run_id": run_id}
    }

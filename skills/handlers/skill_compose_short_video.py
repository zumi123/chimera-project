import uuid
from typing import Dict, List


def handle(input: Dict) -> Dict:
    """Compose short video skill handler (stub).

    Input contract:
    {
      "clips": [ { "asset_path": "string", "start": number, "end": number } ],
      "script": "string",
      "template": "string" (optional)
    }

    Output must follow `specs/schemas/skill_compose_short_video.schema.json`.
    """
    run_id = str(uuid.uuid4())
    # Minimal stub: assume composition succeeded and return asset path
    return {
        "status": "ok",
        "final_asset_path": "/tmp/final_short_video.mp4",
        "duration_seconds": 30,
        "render_log": {"steps": ["trim","render","mux"]},
        "trace": {"spec_version": "0.1", "run_id": run_id}
    }

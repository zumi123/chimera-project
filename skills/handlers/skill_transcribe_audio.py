import uuid
from typing import Dict


def handle(input: Dict) -> Dict:
    """Transcribe audio skill handler (stub).

    Input contract: { "asset_path": "string", "language_hint": "string" }
    Output must follow `specs/schemas/skill_transcribe_audio.schema.json`.
    """
    run_id = str(uuid.uuid4())
    # Minimal stub: return a short transcript with one segment
    return {
        "status": "ok",
        "transcript": "Hello world",
        "segments": [{"start": 0.0, "end": 1.2, "text": "Hello world"}],
        "trace": {"spec_version": "0.1", "run_id": run_id}
    }

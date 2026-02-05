# Skills — Project Chimera

Overview
--------
Skills are self-contained runtime capabilities agents invoke. Each skill must declare a stable Input/Output JSON contract, version, and failure modes.

Critical Skills (initial)
------------------------

1) `skill_download_video`
- Purpose: Download a video asset given a source URL.
- Input
  {
    "source_url": "string",
    "max_duration_seconds": integer (optional)
  }
- Output
  {
    "status": "ok|error",
    "asset_path": "string",
    "duration_seconds": integer,
    "metadata": { }
  }
- Errors: `unreachable`, `unsupported_format`, `exceeds_duration`

2) `skill_transcribe_audio`
- Purpose: Produce timestamped transcription from an audio/video asset.
- Input
  {
    "asset_path": "string",
    "language_hint": "string" (optional)
  }
- Output
  {
    "status": "ok|error",
    "transcript": "string",
    "segments": [ { "start": number, "end": number, "text": "string" } ]
  }
- Errors: `audio_too_short`, `low_confidence`

3) `skill_compose_short_video`
- Purpose: Assemble a short video from clips, overlays, and captions.
- Input
  {
    "clips": [ { "asset_path": "string", "start": number, "end": number } ],
    "script": "string",
    "template": "string" (optional)
  }
- Output
  {
    "status": "ok|error",
    "final_asset_path": "string",
    "duration_seconds": integer,
    "render_log": { }
  }
- Errors: `render_failed`, `missing_asset`

Versioning & Contracts
-----------------------
- Every skill must include a `version` field and a `spec_ref` pointing to the relevant `specs/` file.

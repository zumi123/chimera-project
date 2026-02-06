def handle(input):
    """Stub skill: returns a minimal success payload.

    Real implementations should download the asset and return local path and metadata.
    """
    return {
        "status": "ok",
        "asset_path": "/tmp/example_video.mp4",
        "duration_seconds": 30,
        "metadata": {}
    }

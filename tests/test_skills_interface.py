def test_skill_download_video_interface_exists():
    # Implementation expected at skills/skill_download_video.py with callable entrypoint `handle`
    from skills.skill_download_video import handle
    assert callable(handle)

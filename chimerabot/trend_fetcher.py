def fetch_trends(request):
    """Stub implementation: returns intentionally malformed response to drive schema test failure.

    The real implementation should query platform APIs and return the structure defined
    in `specs/schemas/trend_fetcher.schema.json`.
    """
    # Intentionally return wrong types to create a failing test (TDD placeholder)
    return {
        "spec_version": "0.1",
        "timestamp": "2026-02-06T00:00:00Z",
        "trends": [
            {
                "id": "t1",
                "title": "Example Trend",
                "engagement_score": "high",  # should be a number
                "sample_media_url": "not_a_valid_uri"
            }
        ]
    }

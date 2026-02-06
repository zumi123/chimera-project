import json
import pathlib
import jsonschema

schema_path = pathlib.Path(__file__).parent.parent / "specs" / "schemas" / "trend_fetcher.schema.json"


def test_trend_fetcher_response_matches_schema():
    schema = json.loads(schema_path.read_text())
    # Implementation expected: chimerabot.trend_fetcher.fetch_trends
    from chimerabot.trend_fetcher import fetch_trends

    req = {"platform": "youtube", "region": "us", "limit": 1}
    resp = fetch_trends(req)
    jsonschema.validate(instance=resp, schema=schema)

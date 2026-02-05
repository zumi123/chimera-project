# Technical Specifications — Project Chimera

API Contracts
-------------

1) Trend Fetcher

Request (GET /trends)
{
  "platform": "string", // "youtube", "tiktok", "instagram"
  "region": "string",
  "limit": integer
}

Response
{
  "spec_version": "string",
  "timestamp": "ISO8601",
  "trends": [
    {
      "id": "string",
      "title": "string",
      "engagement_score": number,
      "sample_media_url": "string"
    }
  ]
}

2) Skill Invocation Interface (generic)

Request
{
  "skill": "string",
  "version": "string",
  "input": { }
}

Response
{
  "status": "ok|error",
  "output": { },
  "trace": { "spec_version": "string", "run_id": "uuid" }
}


Database Schema (ERD - textual)
-------------------------------
- Table: videos
  - id (uuid)
  - source_url (text)
  - title (text)
  - duration_seconds (int)
  - created_at (timestamp)
  - metadata_json (jsonb)

- Table: trends
  - id (uuid)
  - platform (text)
  - keyword (text)
  - fetched_at (timestamp)
  - payload_json (jsonb)

Indexes: videos(source_url), trends(platform, keyword)

Schema Rationale
-----------------
Use a SQL DB with JSONB fields (Postgres) to keep strong relational guarantees while allowing flexible metadata for high-velocity video attributes.

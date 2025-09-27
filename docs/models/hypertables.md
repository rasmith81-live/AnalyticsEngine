# TimescaleDB Hypertable Models

This document outlines the database schemas for the TimescaleDB hypertables used in the platform.

## `NewsArticle`

**Table Name:** `newsarticle`

**Fields:**

- `source`: `Mapped[str]`
- `title`: `Mapped[str]`
- `content`: `Mapped[str]`
- `published_at`: `Mapped[datetime]`
- `related_tickers`: `Mapped[List[str]]`
- `article_type`: `Mapped[str]`
- `sentiment`: `Mapped[float]`


# TimescaleDB Hypertable Models

This document outlines the database schemas for the TimescaleDB hypertables used in the platform.

## `MarketData`

**Table Name:** `marketdata`

**Fields:**

- `symbol`: `Mapped[str]`
- `price`: `Mapped[float]`
- `volume`: `Mapped[int]`
- `timestamp`: `Mapped[datetime]`

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


# Spotify Listening Analysis

A data analysis project exploring personal Spotify streaming history to uncover listening patterns, preferences, and trends.

## Overview

This project analyzes Spotify streaming data to provide insights into listening behavior, including top artists, albums, tracks, temporal patterns, and music discovery habits.

## Analysis Sections

1. **Data Preparation** — Cleaning and structuring raw streaming data
2. **Top Artists** — Identifying most-played artists
3. **Top Albums** — Analyzing album listening patterns
4. **Top Tracks** — Highlighting frequently played songs
5. **Listening Patterns** — Examining temporal trends (hourly, daily, weekly)
6. **Music Discovery** — Tracking new release vs. catalog listening
7. **Summary** — Key insights and personalized recommendations

## Key Insights

- **Total Listening**: 22,924 minutes (382 hours) across 15,290 tracks
- **Peak Activity**: Fridays at 12 PM
- **Discovery Rate**: 94% new releases (< 1 year old)
- **Average Usage**: 58 minutes per day over 396 active days

## Requirements

```
pandas
matplotlib
numpy
```

## Usage

Run the Jupyter notebook to analyze your own Spotify data:

```bash
jupyter notebook main.ipynb
```

Replace the data source with your Spotify streaming history export (available through Spotify account settings).

## Data Source

Spotify streaming history can be requested from your Spotify account privacy settings. The analysis expects CSV format with fields: timestamp, platform, minutes played, country, track name, artist name, and album name.

## License

MIT

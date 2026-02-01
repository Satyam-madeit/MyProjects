# Spotify Listening Analysis
A data analysis project exploring personal Spotify streaming history to uncover listening patterns, preferences, and trends.

## Overview
This project analyzes Spotify streaming data to provide insights into listening behavior, including top artists, albums, tracks, temporal patterns, and music discovery habits. Results are presented through an interactive **Streamlit dashboard** with a clean, dark-themed UI.

## Analysis Sections
1. **Data Preparation** — Cleaning and structuring raw streaming JSON data
2. **Listening Behavior** — Overview stats: total hours, tracks, active days, and daily averages
3. **Top Artists** — Identifying the 15 most-played artists
4. **Top Albums** — Analyzing album listening patterns
5. **Top Tracks** — Highlighting the 15 most frequently played songs
6. **Platform Distribution** — Breakdown of listening across platforms
7. **Listening Patterns** — Examining temporal trends (hourly and weekly)
8. **Music Discovery** — Tracking new release vs. older catalog listening
9. **Summary** — Key insights and personalized recommendations

## Key Insights
- **Total Listening**: 22,924 minutes (382 hours) across 15,290 tracks
- **Peak Activity**: Fridays at 12 PM
- **Discovery Rate**: 94% new releases (< 1 year old)
- **Average Usage**: 58 minutes per day over 396 active days

## Requirements
```
pandas
plotly
streamlit
```

## Usage

### Streamlit Dashboard (Recommended)
Install dependencies and launch the app:
```bash
pip install pandas plotly streamlit
streamlit run app.py
```
Upload your `Streaming_History_Audio.json` file directly in the browser to generate the dashboard.

### Jupyter Notebook
The original analysis is also available as a notebook:
```bash
jupyter notebook main.ipynb
```

## Data Source
Spotify streaming history can be requested from your account privacy settings at [Spotify Privacy](https://www.spotify.com/privacy). The dashboard expects the raw **JSON** export (`Streaming_History_Audio_*.json`) — no manual conversion needed.

## Project Structure
```
├── app.py                                  # Streamlit dashboard
├── main.ipynb                              # Jupyter notebook analysis
└── README.md                               # This file
```

## License
MIT

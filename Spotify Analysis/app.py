import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import json

# ─────────────────────────────────────────────
# THEME & STYLING
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Spotify Listening Insights",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GREEN = "#1DB954"
GREEN_DARK = "#158a3e"
BG_DARK = "#0f0f0f"
CARD_BG = "#1a1a1a"
CARD_BORDER = "#2a2a2a"
TEXT_PRIMARY = "#ffffff"
TEXT_SECONDARY = "#a8a8a8"
TEXT_MUTED = "#6b6b6b"

st.markdown(f"""
<style>
    /* ── Base ── */
    .stApp {{
        background-color: {BG_DARK};
        color: {TEXT_PRIMARY};
        font-family: 'Segoe UI', system-ui, sans-serif;
    }}
    .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }}

    /* ── Header ── */
    .header-wrap {{
        text-align: center;
        padding: 2.4rem 0 1.6rem;
        border-bottom: 1px solid {CARD_BORDER};
        margin-bottom: 2rem;
    }}
    .header-wrap h1 {{
        font-size: 2.2rem;
        font-weight: 700;
        color: {TEXT_PRIMARY};
        margin: 0;
        letter-spacing: -0.5px;
    }}
    .header-wrap p {{
        color: {TEXT_MUTED};
        font-size: 0.88rem;
        margin: 0.4rem 0 0;
    }}
    .green-dot {{
        display: inline-block;
        width: 8px; height: 8px;
        border-radius: 50%;
        background: {GREEN};
        margin-right: 8px;
        vertical-align: middle;
    }}

    /* ── Stat Cards ── */
    .stat-row {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        margin-bottom: 2rem;
    }}
    .stat-card {{
        background: {CARD_BG};
        border: 1px solid {CARD_BORDER};
        border-radius: 12px;
        padding: 1.4rem 1.2rem;
        transition: border-color 0.2s;
    }}
    .stat-card:hover {{
        border-color: {GREEN};
    }}
    .stat-label {{
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: {TEXT_MUTED};
        margin-bottom: 0.5rem;
    }}
    .stat-value {{
        font-size: 1.7rem;
        font-weight: 700;
        color: {TEXT_PRIMARY};
    }}
    .stat-sub {{
        font-size: 0.75rem;
        color: {TEXT_SECONDARY};
        margin-top: 0.25rem;
    }}

    /* ── Section Title ── */
    .section-title {{
        font-size: 1rem;
        font-weight: 600;
        color: {TEXT_PRIMARY};
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid {CARD_BORDER};
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    /* ── Plotly container fix ── */
    .plotly-chart {{
        background: {CARD_BG};
        border: 1px solid {CARD_BORDER};
        border-radius: 12px;
        padding: 0.8rem;
        margin-bottom: 1.2rem;
    }}

    /* ── Table ── */
    .stDataframe {{
        background: {CARD_BG} !important;
    }}
    table {{
        background: {CARD_BG} !important;
        color: {TEXT_PRIMARY} !important;
        border-collapse: collapse;
        width: 100%;
    }}
    th {{
        color: {TEXT_MUTED} !important;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-bottom: 1px solid {CARD_BORDER} !important;
        padding: 0.6rem 0.8rem !important;
        text-align: left !important;
        background: transparent !important;
    }}
    td {{
        padding: 0.55rem 0.8rem !important;
        border-bottom: 1px solid {CARD_BORDER} !important;
        font-size: 0.85rem;
        color: {TEXT_PRIMARY} !important;
    }}
    tr:hover td {{
        background: rgba(29,185,84,0.06) !important;
    }}

    /* ── Selectbox / Sidebar ── */
    .stSelectbox label, .stSidebar label {{
        color: {TEXT_SECONDARY} !important;
        font-size: 0.78rem !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }}
    .stSelectbox [data-baseid] {{
        background: {CARD_BG} !important;
        border: 1px solid {CARD_BORDER} !important;
        color: {TEXT_PRIMARY} !important;
        border-radius: 8px;
    }}

    /* ── Hide Streamlit chrome ── */
    #MainMenu, footer, .reportview-container .main .block-container:first-of-type {{
        visibility: hidden;
    }}
    .stDeployButton {{ display: none; }}

    /* ── Upload box ── */
    .stFileUploader {{
        border: 1px dashed {CARD_BORDER};
        border-radius: 12px;
        padding: 1rem;
        background: {CARD_BG};
    }}
    .stFileUploader label {{
        color: {TEXT_SECONDARY} !important;
    }}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# DATA LOADING
# ─────────────────────────────────────────────
@st.cache_data
def load_and_clean(raw_bytes: bytes) -> pd.DataFrame:
    data = json.loads(raw_bytes.decode("utf-8"))
    df = pd.DataFrame(data)

    drop_cols = [
        c for c in [
            'reason_start','reason_end','ip_addr','shuffle','skipped',
            'offline','offline_timestamp','incognito_mode','episode_name',
            'audiobook_uri','audiobook_chapter_uri','spotify_track_uri',
            'episode_show_name','spotify_episode_uri','audiobook_title',
            'audiobook_chapter_title'
        ] if c in df.columns
    ]
    df.drop(columns=drop_cols, inplace=True, errors="ignore")

    rename_map = {
        'conn_country': 'Country',
        'master_metadata_album_artist_name': 'Artist',
        'master_metadata_track_name': 'Track',
        'master_metadata_album_album_name': 'Album',
    }
    df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns}, inplace=True)

    df['minutes_played'] = df['ms_played'] / 60000
    df.drop(columns=['ms_played'], inplace=True, errors="ignore")
    df['ts'] = pd.to_datetime(df['ts'])
    df['Year'] = df['ts'].dt.year
    df['Hour'] = df['ts'].dt.hour
    df['Day'] = df['ts'].dt.day_name()
    df['platform'] = df['platform'].fillna('Unknown') if 'platform' in df.columns else 'Unknown'
    return df


# ─────────────────────────────────────────────
# PLOTLY DEFAULTS
# ─────────────────────────────────────────────
def base_layout(**kwargs):
    # pull axis overrides safely
    xaxis_custom = kwargs.pop("xaxis", {})
    yaxis_custom = kwargs.pop("yaxis", {})

    # base axis configs
    xaxis_cfg = {
        "showgrid": False,
        "showline": False,
        "title_font": dict(color=TEXT_MUTED, size=11),
    }
    yaxis_cfg = {
        "showgrid": True,
        "gridcolor": "#2a2a2a",
        "showline": False,
        "title_font": dict(color=TEXT_MUTED, size=11),
    }

    # override safely (NO duplicate keys)
    xaxis_cfg.update(xaxis_custom)
    yaxis_cfg.update(yaxis_custom)

    return go.Layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=TEXT_SECONDARY, size=11),
        margin=dict(l=16, r=16, t=40, b=40),

        xaxis=xaxis_cfg,
        yaxis=yaxis_cfg,

        hovermode="x unified",
        hoverlabel=dict(
            bgcolor=CARD_BG,
            bordercolor=CARD_BORDER,
            font=dict(size=12, color=TEXT_PRIMARY),
        ),

        **kwargs
    )



def chart_wrap(fig):
    st.markdown('<div class="plotly-chart">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# APP ENTRY
# ─────────────────────────────────────────────

# ── Header ──
st.markdown("""
<div class="header-wrap">
  <h1><span class="green-dot"></span>Spotify Listening Insights</h1>
  <p>Upload your Spotify streaming history JSON to explore your listening patterns</p>
</div>
""", unsafe_allow_html=True)

# ── Upload ──
uploaded = st.file_uploader(
    "Drop your Streaming History Audio JSON file here",
    type=["json"],
    label_visibility="visible",
)

if not uploaded:
    st.markdown(f"""
    <div style="margin-top:3rem; text-align:center; color:{TEXT_MUTED}; font-size:0.85rem;">
        👆 Upload your <b style="color:{TEXT_SECONDARY}">Streaming_History_Audio.json</b> file above to get started.
    </div>
    """, unsafe_allow_html=True)
else:
  # ── Load ──
  df = load_and_clean(uploaded.getvalue())

  # ─────────────────────────────────────────────
  # KPI CARDS
  # ─────────────────────────────────────────────
  total_min = df['minutes_played'].sum()
  total_tracks = len(df)
  active_days = df['ts'].dt.date.nunique()
  avg_per_day = total_min / max(active_days, 1)

  st.markdown(f"""
  <div class="stat-row">
    <div class="stat-card">
      <div class="stat-label">Total Hours</div>
      <div class="stat-value">{total_min/60:,.0f}<span style="font-size:1rem;color:{TEXT_MUTED}">h</span></div>
      <div class="stat-sub">{total_min:,.0f} minutes</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Tracks Played</div>
      <div class="stat-value">{total_tracks:,}</div>
      <div class="stat-sub">unique sessions</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Active Days</div>
      <div class="stat-value">{active_days:,}</div>
      <div class="stat-sub">days with activity</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Daily Average</div>
      <div class="stat-value">{avg_per_day:.0f}<span style="font-size:1rem;color:{TEXT_MUTED}">min</span></div>
      <div class="stat-sub">minutes per day</div>
    </div>
  </div>
  """, unsafe_allow_html=True)

  # ─────────────────────────────────────────────
  # ROW 1 — Tracks by Year  |  Platform Split
  # ─────────────────────────────────────────────
  col1, col2 = st.columns([3, 2], gap="medium")

  with col1:
      st.markdown('<div class="section-title"><span class="green-dot"></span>Tracks by Year</div>', unsafe_allow_html=True)
      yc = df['Year'].value_counts().sort_index()
      fig = go.Figure(
          data=[go.Bar(
              x=yc.index.astype(str), y=yc.values,
              marker_color=GREEN,
              marker_line=dict(color=GREEN_DARK, width=1),
              text=yc.values, textposition="outside",
              textfont=dict(color=TEXT_SECONDARY, size=11),
              hovertemplate="<b>%{x}</b><br>%{y:,} tracks<extra></extra>",
          )],
          layout=base_layout(title_text="", yaxis_title="Tracks")
      )
      chart_wrap(fig)

  with col2:
      st.markdown('<div class="section-title"><span class="green-dot"></span>Platform Distribution</div>', unsafe_allow_html=True)
      pc = df['platform'].value_counts()
      colors_pie = [GREEN, "#158a3e", "#0e6b2f", "#a8a8a8", "#6b6b6b"]
      fig = go.Figure(
          data=[go.Pie(
              labels=pc.index, values=pc.values,
              marker_colors=colors_pie[:len(pc)],
              textinfo="label+percent",
              textfont=dict(color=TEXT_PRIMARY, size=11),
              hovertemplate="<b>%{label}</b><br>%{value:,} plays (%{percent})<extra></extra>",
              hole=0.4,
          )],
          layout=go.Layout(
              paper_bgcolor="rgba(0,0,0,0)",
              plot_bgcolor="rgba(0,0,0,0)",
              margin=dict(l=16, r=16, t=10, b=10),
              showlegend=False,
              font=dict(color=TEXT_SECONDARY, size=11),
              hoverlabel=dict(bgcolor=CARD_BG, bordercolor=CARD_BORDER, font=dict(size=12, color=TEXT_PRIMARY)),
          )
      )
      chart_wrap(fig)

  # ─────────────────────────────────────────────
  # ROW 2 — Top Artists  |  Top Albums  |  Top Tracks
  # ─────────────────────────────────────────────
  TOP_N = 15
  top_artists = df['Artist'].value_counts().head(TOP_N)
  top_albums = df['Album'].value_counts().head(TOP_N)
  top_tracks = df['Track'].value_counts().head(TOP_N)

  tabs = st.tabs(["🎤 Top Artists", "💿 Top Albums", "🎵 Top Tracks"])

  for tab, series, title in zip(tabs, [top_artists, top_albums, top_tracks],
                                 ["Artists", "Albums", "Tracks"]):
      with tab:
          # Truncate long labels for chart, keep original for hover
          max_len = 28
          short = series.index.map(lambda x: (x[:max_len] + "…") if len(str(x)) > max_len else x)
          fig = go.Figure(
              data=[go.Bar(
                  y=short[::-1], x=series.values[::-1],
                  orientation="h",
                  marker_color=[GREEN if i == 0 else "#2a4a2a" for i in range(len(series))],
                  text=series.values[::-1],
                  textposition="outside",
                  textfont=dict(color=TEXT_SECONDARY, size=10),
                  customdata=series.index[::-1],
                  hovertemplate="<b>%{customdata}</b><br>%{x:,} plays<extra></extra>",
              )],
              layout=base_layout(
                  title_text=f"Top {TOP_N} {title}",
                  title_font=dict(color=TEXT_PRIMARY, size=13),
                  xaxis=dict(showgrid=True, gridcolor="#2a2a2a", showline=False, title_text="Plays"),
                  yaxis=dict(showgrid=False, showline=False, tickfont=dict(size=10.5, color=TEXT_SECONDARY)),
                  height=480,
                  bargap=0.3,
              )
          )
          chart_wrap(fig)

  # ─────────────────────────────────────────────
  # ROW 3 — Hourly Activity  |  Weekly Patterns
  # ─────────────────────────────────────────────
  col1, col2 = st.columns(2, gap="medium")

  with col1:
      st.markdown('<div class="section-title"><span class="green-dot"></span>Hourly Listening</div>', unsafe_allow_html=True)
      hourly = df['Hour'].value_counts().sort_index()
      peak_h = hourly.idxmax()
      fig = go.Figure(
          data=[go.Bar(
              x=[f"{h:02d}:00" for h in hourly.index],
              y=hourly.values,
              marker_color=[GREEN if h == peak_h else "#2a4a2a" for h in hourly.index],
              hovertemplate="<b>%{x}</b><br>%{y:,} plays<extra></extra>",
          )],
          layout=base_layout(title_text="", xaxis_title="Hour", yaxis_title="Plays",
                             xaxis_tickfont=dict(size=9))
      )
      chart_wrap(fig)

  with col2:
      st.markdown('<div class="section-title"><span class="green-dot"></span>Weekly Patterns</div>', unsafe_allow_html=True)
      day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
      weekly = df['Day'].value_counts().reindex(day_order).fillna(0).astype(int)
      peak_d = weekly.idxmax()
      fig = go.Figure(
          data=[go.Bar(
              x=weekly.index, y=weekly.values,
              marker_color=[GREEN if d == peak_d else "#2a4a2a" for d in weekly.index],
              hovertemplate="<b>%{x}</b><br>%{y:,} plays<extra></extra>",
          )],
          layout=base_layout(title_text="", xaxis_title="Day", yaxis_title="Plays",
                             xaxis_tickfont=dict(size=9.5))
      )
      chart_wrap(fig)

  # ─────────────────────────────────────────────
  # ROW 4 — Discovery Rate
  # ─────────────────────────────────────────────
  st.markdown('<div class="section-title"><span class="green-dot"></span>Discovery Rate</div>', unsafe_allow_html=True)

  current_year = df['Year'].max()
  df['IsNew'] = df['Year'] >= (current_year - 1)
  new_ct = int(df['IsNew'].sum())
  old_ct = int((~df['IsNew']).sum())
  new_pct = new_ct / total_tracks * 100

  col1, col2 = st.columns([1, 3], gap="medium")

  with col1:
      fig = go.Figure(
          data=[go.Pie(
              labels=["New Releases", "Older Tracks"],
              values=[new_ct, old_ct],
              marker_colors=[GREEN, "#2a2a2a"],
              textinfo="percent",
              textfont=dict(color=TEXT_PRIMARY, size=13, family="sans-serif"),
              hovertemplate="<b>%{label}</b><br>%{value:,} (%{percent})<extra></extra>",
              hole=0.5,
          )],
          layout=go.Layout(
              paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
              margin=dict(l=0, r=0, t=10, b=10), showlegend=False,
              font=dict(color=TEXT_SECONDARY),
              hoverlabel=dict(bgcolor=CARD_BG, bordercolor=CARD_BORDER, font=dict(size=12, color=TEXT_PRIMARY)),
          )
      )
      chart_wrap(fig)

  with col2:
      st.markdown(f"""
      <div style="display:flex; gap:2rem; align-items:center; height:100%; padding-top:1rem;">
        <div style="background:{CARD_BG}; border:1px solid {CARD_BORDER}; border-radius:12px; padding:1.4rem 1.8rem; flex:1;">
          <div style="font-size:0.7rem; text-transform:uppercase; letter-spacing:1.2px; color:{TEXT_MUTED};">New Releases <span style="color:{GREEN}">&lt; 1 yr</span></div>
          <div style="font-size:2rem; font-weight:700; color:{GREEN}; margin-top:0.3rem;">{new_pct:.1f}%</div>
          <div style="font-size:0.77rem; color:{TEXT_SECONDARY}; margin-top:0.15rem;">{new_ct:,} tracks</div>
        </div>
        <div style="background:{CARD_BG}; border:1px solid {CARD_BORDER}; border-radius:12px; padding:1.4rem 1.8rem; flex:1;">
          <div style="font-size:0.7rem; text-transform:uppercase; letter-spacing:1.2px; color:{TEXT_MUTED};">Older Tracks</div>
          <div style="font-size:2rem; font-weight:700; color:{TEXT_SECONDARY}; margin-top:0.3rem;">{100-new_pct:.1f}%</div>
          <div style="font-size:0.77rem; color:{TEXT_SECONDARY}; margin-top:0.15rem;">{old_ct:,} tracks</div>
        </div>
      </div>
      """, unsafe_allow_html=True)

  # ─────────────────────────────────────────────
  # FOOTER
  # ─────────────────────────────────────────────
  st.markdown(f"""
  <div style="margin-top:3rem; padding-top:1.2rem; border-top:1px solid {CARD_BORDER};
       text-align:center; color:{TEXT_MUTED}; font-size:0.72rem;">
    Spotify Listening Insights &nbsp;·&nbsp; Built with Streamlit &nbsp;·&nbsp; Data covers {df['Year'].min()}–{df['Year'].max()}
  </div>
  """, unsafe_allow_html=True)

# Luna 🌙

A Python-based voice assistant that listens to your commands and executes them. Wake her up by saying "Luna" and let her handle your tasks.

## Features

**Voice Control** - Hands-free operation with wake word detection

**Web Browsing** - Opens 30+ pre-configured websites or searches anything on Google

**Music Player** - Spotify integration with smart song search and playback

**App Launcher** - Launch any application installed on your system

**AI Conversations** - Powered by Google Gemini for intelligent responses

**System Info** - Get current time, date, and day of the week

## Installation

### Requirements

Python 3.7 or higher

### Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 requests gtts pygame google-generativeai AppOpener spotipy pyaudio
```

**Note for Windows users:** You may need to install PyAudio separately:
```bash
pip install pipwin
pipwin install pyaudio
```

## Setup

### 1. Google Gemini API (Required)

- Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
- Create a new API key
- Replace `Your API Key Here` on line 109 with your key

```python
client = genai.Client(api_key="your_actual_api_key_here")
```

### 2. Spotify Integration (Optional)

Only needed if you want music playback features.

- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create a new app
- Copy your Client ID and Client Secret
- Set Redirect URI to: `http://127.0.0.1:8888/callback`
- Update lines 18-19 in the code:

```python
SPOTIPY_CLIENT_ID = 'your_client_id_here'
SPOTIPY_CLIENT_SECRET = 'your_client_secret_here'
```

## Running Luna

```bash
python luna.py
```

Wait for "Initializing Luna...." then say **"Luna"** to activate.

## Command Guide

### Wake Word Variations
Luna recognizes: "Luna", "Lunah", "Lunar", "Lona", "Loona"

### Opening Websites

**Syntax:** "Open [website name]"

```
"Luna, open YouTube"
"Luna, open GitHub" 
"Luna, open Netflix"
```

Supported sites include: Google, YouTube, Facebook, Twitter, Instagram, Reddit, LinkedIn, GitHub, Netflix, Amazon, Stack Overflow, LeetCode, GeeksforGeeks, Kaggle, ChatGPT, Gmail, and more.

### Playing Music

**Syntax:** "Play [song name]"

```
"Luna, play Bohemian Rhapsody"
"Luna, play Shape of You by Ed Sheeran"
"Luna, play music" (opens Spotify)
```

Luna searches for the song, shows you the top 5 results, and automatically plays the best match.

**Requirements:**
- Spotify desktop app must be installed and logged in
- First run will open browser for Spotify authentication

### Launching Applications

**Syntax:** "Start [application name]"

```
"Luna, start Notepad"
"Luna, start Chrome"
"Luna, start Visual Studio Code"
```

Luna uses fuzzy matching to find the closest app if the exact name isn't found.

### Google Search

**Syntax:** "Search for [query]"

```
"Luna, search for Python tutorials"
"Luna, search for best restaurants near me"
```

### Getting Time & Date

```
"Luna, what is the time?"
"Luna, what is the date?"
"Luna, what is the day?"
```

### AI Conversations

Ask Luna anything else and she'll use Google Gemini to respond:

```
"Luna, what is quantum physics?"
"Luna, tell me a joke"
"Luna, how do I center a div?"
"Luna, explain recursion"
```

## How It Works

1. **Wake Word Detection** - Continuously listens for "Luna" with 1-second phrases
2. **Command Listening** - Once activated, listens for up to 5 seconds for your command
3. **Speech Recognition** - Converts your voice to text using Google Speech Recognition
4. **Command Processing** - Analyzes the command and executes the appropriate action
5. **Text-to-Speech** - Responds using Google TTS with natural-sounding voice

## Troubleshooting

**"Error; [Errno -9988] Stream closed"**
- Your microphone isn't working or isn't set as default
- Check microphone permissions in system settings

**"Rate limit exceeded"**
- You've hit the Gemini API quota
- Wait 30-60 seconds before trying again
- Free tier has daily limits

**Spotify not playing**
- Make sure Spotify desktop app is running
- Check if you're logged in
- First-time setup requires browser authentication

**Luna doesn't hear me**
- Speak clearly and closer to the microphone
- Reduce background noise
- Check microphone volume in system settings

**App won't open**
- Make sure you say "start" before the app name
- Try using the exact application name
- Some apps may require admin privileges

## Technical Details

**Speech Recognition:** Google Speech Recognition API

**Text-to-Speech:** Google Text-to-Speech (gTTS) with pygame for audio playback

**AI Model:** Google Gemini 3 Flash Preview

**Audio Processing:** SpeechRecognition library with PyAudio backend

**Spotify API:** Spotipy with OAuth2 authentication

## Future Improvements

- Multi-language support
- Custom wake word training
- Integration with smart home devices
- Calendar and reminder features
- Email reading and sending
- Weather information
- News briefings

## Contributing

Feel free to fork this project and submit pull requests. Some areas that need improvement:

- Better error handling
- Offline mode for basic commands
- Custom command creation
- Voice training for better accuracy

## License

This project is open source and available for personal and educational use.

---

**Note:** This project uses various APIs that have usage limits. The free tier of Google Gemini may have rate limits. Spotify requires a Premium account for full playback control.

*Built with Python • Powered by Google Gemini*
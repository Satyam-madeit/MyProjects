# Jarvis Voice Assistant

A Python-based voice assistant inspired by Iron Man's JARVIS, featuring voice recognition, text-to-speech, and AI-powered responses using Google's Gemini API.

## Features

- **Wake Word Activation**: Responds to "Jarvis" as the wake word
- **Voice Recognition**: Understands and processes voice commands
- **Natural Speech Output**: Converts responses to speech using Google Text-to-Speech
- **Website Navigation**: Quick access to popular websites
- **AI-Powered Responses**: Uses Google Gemini API for intelligent conversations
- **Time & Date Information**: Provides current time, date, and day

## Prerequisites

- Python 3.7 or higher
- Microphone for voice input
- Internet connection
- Google Gemini API key

## Installation

1. Clone this repository or download the `main.py` file

2. Install required dependencies:

```bash
pip install speechrecognition
pip install pyttsx3
pip install requests
pip install gtts
pip install pygame
pip install google-genai
pip install pyaudio
```

**Note**: If you encounter issues installing `pyaudio`, try:
- **Windows**: `pip install pipwin` then `pipwin install pyaudio`
- **Mac**: `brew install portaudio` then `pip install pyaudio`
- **Linux**: `sudo apt-get install python3-pyaudio`

3. Get a Google Gemini API key:
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key
   - Replace `"YOUR_API_KEY_HERE"` in `main.py` with your actual API key

## Usage

1. Run the program:

```bash
python main.py
```

2. Wait for "Initializing Jarvis...." message

3. Say "Jarvis" to activate the assistant

4. After hearing "Yes Satyam", speak your command

## Supported Commands

### Website Navigation
- "Open Google/Facebook/YouTube/Twitter/Reddit"
- "Open LinkedIn/GitHub/Netflix/Instagram"
- "Open Hotstar/Fancode"
- "Open ChatGPT" or "Open OpenAI"
- "Play music" (opens Spotify)

### Information Queries
- "What is the date?"
- "What is the day?"
- "What is the time?"

### General Queries
Any other question will be processed by the Gemini AI, which can handle:
- General knowledge questions
- Conversations
- Explanations
- And more

## Customization

### Change the User Name
The assistant currently addresses the user as "Satyam". To change this:
1. Find all instances of `"Satyam"` in the code
2. Replace with your preferred name

### Change the Wake Word
To use a different wake word instead of "Jarvis":
1. Locate the line: `if("jarvis" in word.lower()):`
2. Replace `"jarvis"` with your preferred wake word

### Add More Website Commands
Add new website commands in the `processCommand()` function:

```python
elif "open example" in c.lower():
    webbrowser.open("https://example.com")
```

## Troubleshooting

**Microphone Not Working**
- Check system microphone permissions
- Ensure microphone is set as default recording device
- Test microphone with other applications

**API Rate Limiting**
- The free Gemini API has usage limits
- The code includes automatic rate limit handling
- Wait 30-60 seconds if you encounter rate limits

**Speech Recognition Errors**
- Speak clearly and at a moderate pace
- Reduce background noise
- Check internet connection (Google Speech Recognition requires internet)

**Audio Playback Issues**
- Ensure pygame mixer is properly initialized
- Check system audio output settings
- Verify temp.mp3 file permissions

## Project Structure

- `speak()`: Converts text to speech using gTTS and pygame
- `aiProcess()`: Sends queries to Gemini API for AI responses
- `processCommand()`: Processes specific commands and website navigation
- Main loop: Continuously listens for wake word and commands

## API Information

This project uses:
- **Google Speech Recognition**: For voice-to-text conversion
- **Google Text-to-Speech (gTTS)**: For text-to-voice conversion
- **Google Gemini API**: For AI-powered responses

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional command support
- Better error handling
- Multi-language support
- Integration with smart home devices

## Acknowledgments

Inspired by JARVIS from the Iron Man movies and built with Python's amazing ecosystem of libraries for speech recognition and AI integration.
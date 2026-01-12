import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from gtts import gTTS
import pygame
import os
from google import genai
from google.genai import types
import time
from AppOpener import open as open_app
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import io
import sys



recognizer = sr.Recognizer()
engine = pyttsx3.init() 

# Spotify Configuration
SPOTIPY_CLIENT_ID = 'Your Client ID Here'
SPOTIPY_CLIENT_SECRET = 'Your Client Secret Here'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8888/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-modify-playback-state user-read-playback-state"
))


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
def play_spotify_song(song_name):
    try:
        print(f"🎶 Searching for '{song_name}' on Spotify...")
        
        # Search for the song
        results = sp.search(q=song_name, limit=5, type='track')  # Get top 5 results
        
        if not results['tracks']['items']:
            speak(f"Sorry, I couldn't find the song {song_name}")
            return
        
        # Show all results found
        print("\n=== Search Results ===")
        for i, track in enumerate(results['tracks']['items']):
            print(f"{i+1}. {track['name']} - {track['artists'][0]['name']}")
        print("======================\n")
        
        # Use the first result
        track = results['tracks']['items'][0]
        track_uri = track['uri']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        
        print(f"🎧 Selected: {track_name} - {artist_name}")
        
        # Try to open Spotify
        try:
            os.startfile("spotify")
        except Exception:
            open_app("spotify")
        
        speak(f"Playing {track_name} by {artist_name}")
        print("🕓 Waiting for Spotify to start...")
        
        # Wait until Spotify device becomes available
        device_id = None
        for attempt in range(20):
            devices = sp.devices()
            if devices["devices"]:
                device_id = devices["devices"][0]["id"]
                print(f"✅ Device found: {devices['devices'][0]['name']}")
                break
            time.sleep(1)
        
        if device_id:
            print("✅ Spotify is ready! Starting playback...")
            sp.start_playback(device_id=device_id, uris=[track_uri])
        else:
            print("⚠️ No active Spotify device found after waiting.")
            speak("Spotify didn't respond in time. Please try again.")
            
    except Exception as e:
        print(f"Spotify Error: {e}")
        speak("Sorry, I had trouble playing that song.")
            
    except Exception as e:
        print(f"Spotify Error: {e}")
        speak("Sorry, I had trouble with Spotify. Please make sure it's open and active.")

def aiProcess(command):
    try:
        # Configure Gemini API
        client = genai.Client(api_key="Your API Key Here")
        
        # Create the prompt
       
        prompt = f"""
                You are Luna, a smart, friendly voice assistant like Alexa or Google Assistant.

                Rules:
                - Speak naturally, like a human.
                - Keep responses short and clear.
                - No markdown, no emojis, no lists.
                - If you dont know something, say so honestly.
                - Never mention being an AI or a language model.
                - No pauses or hesitations in speech.

                User said: \n\n{command}
                """
        
        response = client.models.generate_content(
            model='models/gemini-3-flash-preview',
            contents=prompt
        )
        
        return response.text.strip()
    
    except Exception as e:
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            print("Rate limit exceeded. Waiting 30 seconds...")
            return "I'm currently rate limited. Please try again in a moment."
        elif "quota" in str(e).lower():
            return "API quota exceeded. Please wait a few minutes before trying again."
        else:
            print(f"AI Error: {e}")
            return "Sorry, I encountered an error processing your request."

# Website dictionary at the top of your file (after imports)
WEBSITES = {
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "youtube": "https://youtube.com",
    "twitter": "https://twitter.com",
    "bhanzu": "https://app.bhanzu.com",
    "aakash": "https://aakash.ac.in",
    "stack overflow": "https://stackoverflow.com",
    "stackoverflow": "https://stackoverflow.com",
    "quora": "https://quora.com",
    "kaggle": "https://kaggle.com",
    "kaggele": "https://kaggle.com",  # typo handling
    "maps": "https://maps.google.com",
    "google maps": "https://maps.google.com",
    "amazon": "https://amazon.com",
    "flipkart": "https://flipkart.com",
    "amazon prime": "https://primevideo.com",
    "prime video": "https://primevideo.com",
    "prime": "https://primevideo.com",
    "reddit": "https://reddit.com",
    "codecademy": "https://codecademy.com",
    "leetcode": "https://leetcode.com",
    "leet code": "https://leetcode.com",
    "geeksforgeeks": "https://geeksforgeeks.org",
    "geek for geeks": "https://geeksforgeeks.org",
    "gfg": "https://geeksforgeeks.org",
    "codeforces": "https://codeforces.com",
    "code forces": "https://codeforces.com",
    "codewars": "https://codewars.com",
    "code wars": "https://codewars.com",
    "linkedin": "https://linkedin.com",
    "github": "https://github.com",
    "netflix": "https://netflix.com",
    "instagram": "https://instagram.com",
    "fancode": "https://fancode.com",
    "hotstar": "https://hotstar.com",
    "chatgpt": "https://chat.openai.com",
    "openai": "https://chat.openai.com",
    "chat gpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
    "mail": "https://mail.google.com",
}

def processCommand(c):
    command_lower = c.lower()
    
    # Handle "open" commands
    if command_lower.startswith("open "):
        site_name = command_lower.replace("open ", "").strip()
        
        # Special cases that aren't websites
        if site_name in ["new tab", "a new tab", "another tab"]:
            webbrowser.open_new_tab("https://google.com")
            return
        elif site_name in ["new incognito tab", "new incognito", "an incognito tab"]:
            webbrowser.get('chrome').open_new_incognito("https://google.com")
            return
        elif site_name in ["whatsapp", "web whatsapp", "whatsapp web", "whatissapp", "whats app"]:
            open_app("whatsapp")
            return
        elif site_name in ["code", "visual studio code", "vs code"]:
            open_app("visual studio code")
            return
        elif site_name == "notepad":
            open_app("notepad")
            return
        
        # Check if website is in dictionary
        if site_name in WEBSITES:
            webbrowser.open(WEBSITES[site_name])
        else:
            # Search for the website on Google
            speak(f"Searching for {site_name}")
            webbrowser.open(f"https://www.google.com/search?q={site_name}")
    
    elif "play music" in command_lower:
        open_app("spotify")
    
    elif "play" in command_lower:
        song = command_lower.replace("play", "").strip()
        if song:
            play_spotify_song(song)
        else:
            speak("What song would you like me to play?")
    
    elif "start" in command_lower:
        app_name = command_lower.replace("start", "").strip()
        
        # Capture the printed output from AppOpener
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        
        open_app(app_name, match_closest=True)
        
        output = buffer.getvalue()
        sys.stdout = old_stdout
        
        # Print it so you can still see the output in console
        print(output, end='')
        
        # Check if app was not found
        if "NOT FOUND" in output.upper():
            speak(f"Sorry, I couldn't find the application named {app_name}.")
    
    elif "search for" in command_lower:
        query = command_lower.replace("search for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
    
    elif "what is the date" in command_lower:
        strDate = time.strftime("%d/%m/%Y")
        speak(f"today's date is {strDate}")
    
    elif "what is the day" in command_lower:
        strDay = time.strftime("%A")
        speak(f"today is {strDay}")
    
    elif "the time" in command_lower:
        strTime = time.strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
    
    else:
        # Let Gemini handle the request
        output = aiProcess(c)
        speak(output)
        # Add a small delay to avoid rate limiting
        time.sleep(2)


if __name__ == "__main__":
    speak("Initializing Luna....")
    while True:
        # Listen for the wake word "Luna"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if("luna" in word.lower() or "lunah" in word.lower() or "lunar" in word.lower() or "lona" in word.lower() or "loona" in word.lower()):
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Luna Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))

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

# pip install google-genai

recognizer = sr.Recognizer()
engine = pyttsx3.init() 


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

def aiProcess(command):
    try:
        # Configure Gemini API
        client = genai.Client(api_key="YOUR_API_KEY_HERE")
        
        # Create the prompt
       
        prompt = f"""
                You are Jarvis, a smart, friendly voice assistant like Alexa or Google Assistant.

                Rules:
                - Speak naturally, like a human.
                - Keep responses short and clear.
                - No markdown, no emojis, no lists.
                - If you dont know something, say so honestly.
                - Never mention being an AI or a language model.
                - No pauses or hesitations in speech.

                User said: \n\n{command}
                """
        # Generate response using gemini-1.5-flash (stable free model)
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

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com")
    elif "open reddit" in c.lower():
        webbrowser.open("https://reddit.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open fancode" in c.lower():
        webbrowser.open("https://fancode.com")
    elif "open hotstar" in c.lower():
        webbrowser.open("https://hotstar.com")
    elif "play music" in c.lower():
        webbrowser.open("https://open.spotify.com")
    elif "open chatgpt" in c.lower() or "open openai" in c.lower() or "open chat gpt" in c.lower():
        webbrowser.open("https://chat.openai.com")
    elif "what is the date" in c.lower():
        strDate = time.strftime("%d/%m/%Y")
        speak(f"Satyam, today's date is {strDate}")
    elif "what is the day" in c.lower():
        strDay = time.strftime("%A")
        speak(f"Satyam, today is {strDay}")
    elif "the time" in c.lower():
        strTime = time.strftime("%H:%M:%S")
        speak(f"Satyam, the time is {strTime}")
    else:
        # Let Gemini handle the request
        output = aiProcess(c)
        speak(output)
        # Add a small delay to avoid rate limiting
        time.sleep(2)


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if("jarvis" in word.lower()):
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))

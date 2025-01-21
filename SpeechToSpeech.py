# Text to Speech

import pyttsx3

engine = pyttsx3.init() #Initialize pyttsx3



# Set properties
rate = engine.getProperty('rate')   # Speed of speech
engine.setProperty('rate', rate-50)  # Reduce the speed by 50 (default is 200)
volume = engine.getProperty('volume')  # Volume level (0.0 to 1.0)
engine.setProperty('volume', volume+0.25)  # Increase volume by 25%


engine.say("Reduce your voice")
engine.runAndWait() #Block while processing all the currently queued commands




# Speech to Text

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Please speak something...")
    # Adjust for ambient noise and record audio
    recognizer.adjust_for_ambient_noise(source, duration=1)
    try:
        # Capture the audio
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        print("Processing your speech...")
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.WaitTimeoutError:
        print("No speech was detected in the given time.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


# Speech to Speech


import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine (pyttsx3)
engine = pyttsx3.init()

# Set text-to-speech properties
rate = engine.getProperty('rate')  # Speed of speech
engine.setProperty('rate', rate - 50)  # Slow down the speech speed
volume = engine.getProperty('volume')  # Volume level (0.0 to 1.0)
engine.setProperty('volume', volume + 0.25)  # Increase volume

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Please speak something...")
    # Adjust for ambient noise and record audio
    recognizer.adjust_for_ambient_noise(source, duration=1)
    try:
        # Capture the audio
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        print("Processing your speech...")
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        
        # Text-to-Speech: Read the recognized text aloud
        engine.say(f"You said: {text}")
        engine.runAndWait()
        
    except sr.WaitTimeoutError:
        print("No speech was detected in the given time.")
        engine.say("No speech was detected.")
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        engine.say("Sorry, I could not understand the audio.")
        engine.runAndWait()
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        engine.say("Could not request results. Please check your internet connection.")
        engine.runAndWait()


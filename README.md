# Text-to-Speech, Speech-to-Text, and Speech-to-Speech Application

This project demonstrates a Python application that integrates text-to-speech, speech-to-text, and speech-to-speech functionalities. It uses the `pyttsx3` library for text-to-speech and the `speech_recognition` library for speech-to-text.

## Features
1. **Text-to-Speech**: Converts a given string into spoken words.
2. **Speech-to-Text**: Converts speech input from the microphone into text using Google Web Speech API.
3. **Speech-to-Speech**: Combines the functionalities of speech-to-text and text-to-speech to respond to user speech input.



## Prerequisites
Ensure you have the following Python libraries installed:

- `pyttsx3`: For text-to-speech conversion.
- `speech_recognition`: For speech-to-text conversion.

Install the libraries using pip if not already installed:
```bash
pip install pyttsx3 SpeechRecognition
```



## Code Explanation
### 1. Text-to-Speech
The `pyttsx3` library is used for text-to-speech conversion. Key steps include:
- Initializing the engine.
- Setting properties such as speech rate and volume.
- Passing a string to be spoken aloud using the `say` method.

### 2. Speech-to-Text
The `speech_recognition` library is used to capture speech input via a microphone and convert it into text:
- The `Recognizer` class initializes the recognizer.
- The `Microphone` class captures audio input.
- Ambient noise is adjusted for accurate recognition using `adjust_for_ambient_noise`.
- The captured audio is processed and converted to text using the Google Web Speech API.

### 3. Speech-to-Speech
Combines text-to-speech and speech-to-text functionality:
- Speech input is captured and recognized.
- The recognized text is read aloud using `pyttsx3`.
- Appropriate error handling provides feedback for situations such as unrecognized input or network issues.



## Usage
### Text-to-Speech
This block of code converts a predefined string into speech:
```python
engine.say("Reduce your voice")
engine.runAndWait()
```

### Speech-to-Text
Captures and processes user speech input:
```python
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    text = recognizer.recognize_google(audio)
    print("You said:", text)
```

### Speech-to-Speech
Converts user speech input into text and then reads the recognized text aloud:
```python
with sr.Microphone() as source:
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    text = recognizer.recognize_google(audio)
    engine.say(f"You said: {text}")
    engine.runAndWait()
```



## Error Handling
The application handles common errors gracefully:
- **TimeoutError**: No speech detected within the given time.
- **UnknownValueError**: Speech was unclear or could not be understood.
- **RequestError**: Issues connecting to the Google Web Speech API (e.g., network problems).



## Notes
- The Google Web Speech API requires an active internet connection.
- Microphone permissions must be granted for audio input.
- Ensure that your microphone is properly configured and functional.


## Future Enhancements
- Add support for multiple languages.
- Include offline speech recognition for environments with limited internet connectivity.
- Provide a graphical user interface (GUI) for enhanced usability.


This project is open-source and available for modification.


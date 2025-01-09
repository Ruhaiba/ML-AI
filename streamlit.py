import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to voice input and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
        except sr.RequestError:
            speak("There seems to be an issue with my speech recognition service.")
        return ""

def jarvis():
    """Main Jarvis function."""
    speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        command = listen()
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I can perform basic tasks like telling the time or opening websites. Let me know how I can help.")

# Run the assistant
if __name__ == "__main__":
    jarvis()


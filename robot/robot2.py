import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def get_voice_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error connecting to the Google API.")
        return None

def speak_response(response_text):
    tts = gTTS(text=response_text, lang="en")
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")

def main():
    print("Voice Command Chat")

    while True:
        command = get_voice_command()

        if command:
            response = f"You said: {command}"
            print(f"Response: {response}")
            speak_response(response)

            if "stop" in command:
                print("Stopping the conversation.")
                break

if __name__ == "__main__":
    main()

# My first voice robot
import speech_recognition as sr
import pyttsx3

def listen_for_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your command.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return ""

def respond_with_voice(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        command = listen_for_command()
        if "hello" in command:
            respond_with_voice("Hello there!")
        elif "how are you" in command:
            respond_with_voice("I'm just a computer program, but I'm functioning well!")
        elif "goodbye" in command:
            respond_with_voice("Goodbye! Have a great day!")
            break
        else:
            respond_with_voice("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()

import speech_recognition as sr
import openai
from gtts import gTTS
import playsound

# Set up your OpenAI API key
<<<<<<< HEAD
openai.api_key = "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"
=======
openai.api_key = "sk-iPe0EJr5SQ53Yk2"
>>>>>>> c9ba933e952a8ec6c2ec852177792be1220154dd

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

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose a different GPT-3.5 engine if needed
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()

def speak_response(response_text):
    tts = gTTS(text=response_text, lang="en")
    tts.save("response.mp3")
    playsound.playsound("response.mp3")

def main():
    print("Voice Command Chat with GPT")
    
    while True:
        command = get_voice_command()
        
        if command:
            gpt_response = chat_with_gpt(command)
            print(f"GPT Response: {gpt_response}")
            
            speak_response(gpt_response)
            
            if "stop" in gpt_response:
                print("Stopping the conversation.")
                break

if __name__ == "__main__":
    main()

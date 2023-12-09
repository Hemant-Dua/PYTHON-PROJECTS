import speech_recognition as sr
import win32com.client

def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query}")
        return query

if __name__ == '__main__':
    print("Good Evening, Boss")
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("Good Evening Boss")

    while True:
        print("Listening...")
        text = listener()

        speaker.Speak(text)
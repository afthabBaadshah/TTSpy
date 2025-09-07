import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

while True:

    print("Welcome")

    while True:
        text = input("Enter what to say: ")
        if text=='q':
            speak.Speak("Bye Bye AK")
            break

        speak.Speak(text)



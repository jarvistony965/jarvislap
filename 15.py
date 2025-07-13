import pyttsx3  # Text to speech library
import speechrecognition as sr  # Speech recognition library
import datetime
import wikipedia
import webbrowser
import aifc
import pywhatkit as kit  # For sending WhatsApp messages
import os
import pyautogui
import sys
from news import speak_news, getNewsUrl

# Initialize the text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Selecting the voice (0 for male, 1 for female)

# Function to speak the given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning sir..!")
    elif 12 <= hour < 18:
        speak("Good afternoon sir..!")
    else:
        speak("Good evening sir..!")
    speak("I am Jarvis")
    speak("sir,how can i assistant you today?")

# Function to take command from microphone
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause threshold for listening
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        speak("say that again sir...")
        return "None"
    
    return query

# Main function to execute commands
def main():
    greet()
    while True:
        query = take_command().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia sir...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'jarvis are you there' in query:
            speak("all time at your service sir..")

        elif 'jarvis who created you' in query:
            speak("satya udisi created me sir..")

        elif 'voice' in query:
            if 'male' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'search' in query:
            speak('sir,What do you want to search for?')
            search =  take_command()
            urL='https://www.google.com/search?q=' + search
            chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)

        elif 'jarvis open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube sir..")

        elif 'jarvis open google' in query:
            webbrowser.open("google.com")
            speak("opening google sir..")
            search = take_command()

        elif 'jarvis whats the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
    
        elif 'jarvis open notepad' in query:
            speak('Opening Notepad sir..')
            os.startfile('notepad.exe')  # Open Notepad

        elif 'jarvis open calculator' in query:
            speak('Opening calculator sir..')
            os.startfile('C:\\Windows\\System32\\calc.exe')
    
        elif 'jarvis tell me a joke' in query:
            speak("Why don't scientists trust atoms? Because they make up everything!")

        elif 'remember that jarvis' in query:
            speak("what should i remember sir")
            rememberMessage = take_command()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything jarvis' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'tell me today news jarvis' in query:
            speak('Off course sir..')
            speak_news() # Call the imported function
            url = getNewsUrl()
            speak('Do you want to see the full news...')
            test = take_command()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')

        elif 'sleep jarvis' in query:
            sys.exit() 

        elif 'good night jarvis' in query:
             speak("good night sir..")
             sys.exit()

        elif 'exit jarvis' in query:
            speak("exiting sir..!")
            break

if __name__ == "__main__":
    main()

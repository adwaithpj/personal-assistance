import pyttsx3
import os
import webbrowser
import sys
import speech_recognition as sr
import datetime
import wikipedia
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme(datetime):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hey Adwaith, Luffy here please let me know how can I help you!")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try: 
            print("recognizing")
            query=r.recognize_google(audio, language='en-in')
            print("user said ", query)
        except Exception as e:
            print(e)
            speak("say that again please")
            return 'none'
        return query


def run_powershell_command(command):
    print(command)
    try:
        # Run the PowerShell command
        result = subprocess.run(command, capture_output=True, text=True)

        # Check the return code
        if result.returncode == 1:
            # Display the output
           print("Output:", result.stdout)
        else:
            # Display the error
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", str(e))

# # Example usage
# input_data = input("Enter data:")
# command = "bard-cli " + '"'+input_data +'"'
# print(command)

if __name__ == "__main__":
    wishme(datetime)
    cond=1
    while cond==1:
        query = takecommand().lower()
        query = "bard-cli " + '"'+query+'"'
        print(query)
        run_powershell_command(query)

        if 'wikipedia' in query:
            speak("searching wikipedia ..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            speak= ('according to wikipedia ')
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.co.in/")
        elif 'open chatgpt' in query:
            webbrowser.open("https://chat.openai.com/")
        elif 'open command prompt' in query:
            os.system('start cmd')
        elif 'goodbye luffy' in query:
            speak("Thank you, have a nice day")
            cond = 0
        
sys.exit()         





import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import requests
import json
import wolframalpha
import pygame
import os


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)


def speak(data):
    voice = 'en-CA-LiamNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(1)
    except Exception as e:
        print()
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Tron. How may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")

    except Exception as e:    
        print("Say that again please...")
        speak("Say that again please") 
        return "None"
    return query
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'who' in query or 'what is the meaning of' in query:
            speak('Searching Wikipedia...')
            query = query.replace("who", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
            print(time)

        elif 'how are you' in query:
            question = query.replace('how are you', '')
            speak('I am doing great. How are you ?')
        
        elif 'fine' in query or 'good' in query:
            speak('Good to see you doing well!')
        
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            joke = speak(joke)
            
        
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
        
        elif 'what is your name' in query:
            speak('I am Tron your person assistant')
        
        elif "what is today's date" in query or 'what is the date today' in query:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak('Todays date is' + current_date)
            print(current_date)
            
        
        elif 'news' in query:
            url = ('https://newsapi.org/v2/top-headlines?'
                    'country=in&'
                    'apiKey=482a0ecaffb54046b23fbcce2fdda923')
            try:
                response = requests.get(url)
            except:
                speak('please check your connection')
            news = json.loads(response.text)

            for new in news['articles']:
                print(str(new['title']), "\n")
                speak(str(new['title']))
                engine.runAndWait()

                speak(str(new['description']))
                print(str(new['description']), "\n")
                
        
        elif 'calculate' in query:
            app_id = "WW875R-R47TRWR79Y"
            client = wolframalpha.Client(app_id)
            ind = query.lower().split().index('calculate')
            text = query.split()[ind + 1:]
            res = client.query(" ".join(text))
            answer = next(res.results).text
            speak('the answer is ' + answer)
            print('the answer is ' + answer)
            
        
        elif 'bye' in query or 'goodbye' in query or 'stop' in query:
            exit()            

        

            
            

        

        
        
            
            




    
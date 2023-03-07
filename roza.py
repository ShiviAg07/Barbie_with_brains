
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
import random
import webbrowser
import os
exit_conditions = (":q", "quit", "exit","stop")
import time
time.clock = time.time

gender = "sir"
myname = "Neha"
if (myname[-1] == 'e' or myname[-1] == 'i' or myname[-1] == 'a') :
    gender= "mam"


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12: 
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<23:
        speak("Good Evening!")

    else:
        speak("Its late"+ gender + ", but I am here.")
        
    speak("my name is Roza. What can I do for you?")
   
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YourEmail@mail.com', 'YourPassword')
    server.sendmail('YourEmail@mail.com', to, content)
    server.close()

def ludo():
    speak("Ludo mode activated, say 'roll' to roll the dice over, and 'exit' to stop ludo mode")
    dice = take_command().lower()
    while 'exit' not in dice:
        if 'throw' or 'roll' in dice:
            speak("trrr")
            rr = random.randrange(1,7,1)
            speak(rr)
        else:
            continue
    speak("exit")

def play_game() :
    speak('okk, i have a game for you, lets play it')
    url = "https://rishabh-441.github.io/MatchStick-Game/"
    webbrowser.open(url)

    
def alphabets_numbers(check):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    learn = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    speak("Repeat after me")
    if (check == 0):
        learn = alphabets
    speak("once again one by one")
    for i in learn:
        speak(i)
        aaaa = take_command().lower()
        while(aaaa!=i):
            print("you spoke : " , aaaa)
            speak("Try Again")
            aaaa = take_command().lower()
            speak("very good")
        if 'stop' in aaaa:
            break

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'roza' in command:
                command = command.replace('roza', '')
                print(command)
                
                
    except:
        pass
    return command


def run_roza():
    command = take_command()
    print(command)

    if command in exit_conditions:
        sr.close()    
    if 'play' in command and 'game' in command:
        play_game()

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
        print(time)

    elif 'learn' in command:
        if ('alphabets' in command):
            alphabets_numbers(0)
        elif ('numbers' in command):
            alphabets_numbers(1)
        else:
            talk('Please say the command again.')

    elif 'code' in command:
            speak("Do you want to code online or offline" +gender)
            newquery = take_command().lower()
            
            if 'online' in newquery:
                speak("Where do you want to code "+gender+ " Hackerrank or code chef")
                newquery1 = take_command().lower()
                if 'hackerrank' in newquery1:
                    webbrowser.open("hackerrank.com")
                elif 'codechef' in newquery1:
                    webbrowser.open("codechef.com")
            
            elif 'offline' in newquery:
                speak("Visual Studio, Android Studio, Unity, or Sublime")
                newquery2 = take_command().lower()
                if 'android' in newquery2:
                    andpath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
                    os.startfile(andpath)
                elif 'visual' in newquery2:
                    vispath = "C:\\Users\\Maverick\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(vispath)
                elif 'sublime' in newquery2:
                    subpath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                    os.startfile(subpath)
                elif 'unity' in newquery2:
                    unipath = "C:\\Program Files\\Unity\\Hub\\Editor\\2019.3.9f1\\Editor\\Unity.exe"
                    os.startfile(unipath)
                speak("Here you go sir")

    elif 'creator' in command:
        speak("I was born when bright minds came together to create a friend just for you")

    elif 'who is' in command or 'what is' in command:
        if ("what is" in command):
            person = command.replace('what is', '')
        else:
            person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'who am i' in command:
        global myname
        speak("your name is" + myname+ "If you don't like it. I can change it yes or no?")
        query= take_command().lower()
        if 'yes' in query:
            speak("Alright! what should I call you?")
            query= take_command().lower()
            speak("okay") 
            myname= query

    elif 'send email' in command:
            try:
                speak("What should i say?")
                content = take_command()
                speak("Whom should i send this to?")
                mailname = take_command().lower().replace(" ", "")
                to = mailname+"@gmail.com"
                print(to)
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                speak("Sorry I could not get it, would you please repeat sir")
                
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'hello' in command:
        talk('Hi!'+ myname)

    elif 'how are you doing' in command:
        talk('I am doing good! how about you?'+myname)

    elif 'bye' in command or 'quit' in command or 'exit' in command or 'stop' in command:
        talk('bye')
        quit()

    elif 'who are you' in command:
        talk('I am your friend Roza. If you need any help just ask, friends always help each other')

    elif 'make me happy' in command:
        talk('lets have some fun! I can find a joke or a song for you')

    elif 'suno' in command:
            speak("haan"+gender+"boliye ji")

    elif 'what' in command and 'doing' in command:
        speak("i am just talking to you with my complete attention")
        
    elif 'emergency' in command:
        speak("Calling...")
        import makecall
        
        
    elif 'chat' in command:
        speak("YES finally lets chat after a long while")
        import chatbot
        speak(f" {chatbot.get_response(command)}")

    else:
        talk("Please speak again")
        take_command()    
            
if __name__ == "__main__":
    wishMe()
    while True :
        run_roza() 
    
        
        

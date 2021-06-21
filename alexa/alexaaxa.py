import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import pyjokes
import os
import webbrowser





listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command = command.replace('alexa' , '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command().lower()
    print (command)
    if 'run' in command:
       song = command.replace('play' , '')
       talk('playing' + song)
       print (song)

    if 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('current time is'+ time)
    elif 'play music' in command:
        music_dir = 'C:\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[21]))
    elif 'about' in command:
        person = command.replace('about','')
        info  = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'greatest footballer' in command:
        talk('lionel Messi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open youtube' in command:
        webbrowser.open_new("youtube.com")
    elif 'open google' in command:
        webbrowser.open_new("google.com")
    else:
        talk('please repeat')




while True:
    run_alexa()
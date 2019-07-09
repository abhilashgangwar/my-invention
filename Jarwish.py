import pyttsx3
z=pyttsx3.init()

from nltk.tokenize import sent_tokenize
import speech_recognition as sr
import webbrowser
import os
import time
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    print("TIME OVER, THANKS")

try:
    print(r.recognize_google(audio));
    a=(r.recognize_google(audio))
    b=(sent_tokenize(a))
    
    while True:
        for i in b:
            if i=='what is your name':
                z.say('jarwish')
                z.runAndWait()
                print('Jarwish')
                z.say('WHAT IS YOUR NAME')
                print('what is your name')
                z.runAndWait()
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("speak")
            audio = r.listen(source) 
    
            print(r.recognize_google(audio));
            a=(r.recognize_google(audio))
            b=(sent_tokenize(a))
            print(b)
            for i in b:
                if i=='my name is Abhilash':
                    z.say('welcome abhilash')
                    time.sleep(2)
                    z.runAndWait()
                    print('welcome Abhilash')
                elif i=='what is your date of birth':
                    time.sleep(2)
                    z.say('9 june 2019')
                    z.runAndWait()
                    print('9 june 2019')
                elif i=='I want to shutdown my laptop':
                    print('bye laptop is shutting down')
                    z.say('bye laptop is shutting down')
                    time.sleep(2)
                    os.system("shutdown /s /t 1");
                    z.runAndWait()
                elif i=='open Notepad':
                    z.say('opening notepad')
                    print('opening notepad')
                    os.system("Notepad/o /t 1");
                    z.runAndWait()          
                else:
                    z.say('I dont know you fuck off')
                    z.runAndWait()
                    


except:
        pass;

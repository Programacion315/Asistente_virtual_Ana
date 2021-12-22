from bs4 import BeautifulSoup
from pywhatkit.misc import search
import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard
import subprocess as sub


name = "ana"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 145)

sites={
    
        	'google': 'google.com',
            'youtube': 'youtube.com',
            'gif': 'https://github.com/Programacion315',
            'asco de vida': 'ascodevida.com',
            'ascodevida': 'ascodevida.com'
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()

            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass    
    return rec

def run_ana():

    while True:

        rec = listen()
        print(rec)
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo" + music)
            talk("Reproduciendo" + music)
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search + ": " + wiki)
            talk(wiki)

        elif 'abre' in rec:
           
            for site in sites:
                if site in rec:
                    sub.call(f'start brave.exe {sites[site]}', shell=True)

                    if(site == "gif"):
                        talk('Abrindo git')
                    else:
                        talk(f'Abriendo {site}')
                    
        
        elif 'cerrar programa' in rec:
            talk("Hasta pronto") 
            break 


                      

def hola():
     talk("Bienvenido, soy ana, tu asistente virtual en que te puedo ayudar?")

if __name__ == '__main__':

    hola()
    run_ana()

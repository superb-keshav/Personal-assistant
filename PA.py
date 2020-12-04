import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# To change voice: for male=0 and for female=1

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    speak("i am Keshav's personal assistant sir! please tell me how may I help you")

def takecommand():
    # It takes voice from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1    
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp@gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your password")
    server.sendmail("youremail@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()

        #logic for executing tasks
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir="D:\\My phone\\Keshav things\\English songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H;%M;%S")
            speak(f"Sir, the time is{strTime}")
    
        elif "email to keshav" in query:
            try:
                speak("what should say?")
                content=takecommand()
                to= "emailid@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successsfully")
            except Exception as e:
                print(e)
                speak("Sorry my friend Keshav .I am unable to send email") 
   

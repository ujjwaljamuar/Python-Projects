import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(" Its ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(" and today is")
    speak(month)
    speak(date)
    speak(year)


def quit():
    quit()


def wishme():
    speak("Welcome back Sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good AfterNoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    else:
        speak("GoodNight")
    speak("Friday at your Service, How can i help you Sir?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print("query")
    except Exception as e:
        print(e)
        speak("Say that Again Please...")

        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("ujjwalj12222@gmail.com", "chutiyalund")
    server.sendmail("ujjwalj12222@gmail.com", to, content)
    server.close()

def cpu():
    usage= str(psutil.cpu_percent())
    speak("CPU is at "+ usage)

    battery = psutil.sensors_battery()
    speak("battery is at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "send email" in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "niveditajamuar@gmail.com"
                sendEmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to send the email")
        elif "offline" in query:
            quit()
        elif "search in chrome" in query:
            speak("What should i search ?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system(("shutdown - l"))
        elif "shutdown" in query:
            os.system(("shutdown /s /t 1"))
        elif "restart" in query:
            os.system(("shutdown - /r /t 1"))

        elif "play songs" in query:
            songs_dir = "E:\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("what should i remember")
            data = takeCommand()
            speak("you said me to remember that" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" +remember.read())

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()
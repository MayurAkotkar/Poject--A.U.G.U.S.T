import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import cv2
import pyautogui,time
import pyautogui
from playsound import playsound
import pyjokes
import psutil
import smtplib
import PyPDF3
import speedtest
import requests
from keyboard import volumedown
from bs4 import BeautifulSoup
from requests import get
import wikipedia 
from keyboard import volumeup
import webbrowser
import pywhatkit as kit
import wolframalpha
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer , QTime , QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from augustui import Ui_augustui
from pynput.keyboard import Key,Controller
from time import sleep
import ctypes

user32 = ctypes.windll.user32


try:
    app_id = wolframalpha.Client("V2L5HE-E2948WPVJ2")
except Exception:
    print("Some features do not access")

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",130)

def sendEmail(to , content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your gmail" , "your password")
    server.sendmail("recivers email",to,content)
    server.close()

def speak(audio):   # speak function/module of system..help in converting text to voice.
    engine.say(audio)
    engine.runAndWait()

def pdf_reader():
    book = open("C:\\Users\\saksh\\OneDrive\\Desktop\\newfinalaugust\\The Grand Design - Stephen Hawking.pdf",'rb')
    pdfReader = PyPDF3.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of Pages in  the book {pages}")
    speak("Sir please enter page number I have to read")
    pg = int(input("Enter the page numbers:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def click_pic(*args, **kwargs):
    try:
        t = datetime.datetime.now()
        #     Taking a video from the webcam
        camera = cv2.VideoCapture(0)
        #     Taking first 20 frames of the video
        for i in range(20):
            return_value, image = camera.read()
        if not os.path.exists("photos"):
            os.mkdir("photos")
        #     Using 20th frame as the picture and now saving the image as the time in seconds,minute,hour,day and month of the year
        # Giving the camera around 20 frames to adjust to the surroundings for better picture quality
        cv2.imwrite(f"photos/{t.second, t.minute, t.hour, t.day, t.month}_photo.png", image)
        #     As soon as the image is saved we will stop recording
        del camera
        print(f"Photo taken: photos/{t.second, t.minute, t.hour, t.day, t.month}_photo.png")
        return "Photo taken"
    except Exception as e:
        return "Error: " + str(e) + "\n Unable to take photo"


def wish():        # gretting module...wish user according to time.
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and  hour<=12):
        speak("Good morning Sir")
    elif(hour >=12 and   hour<=16):
        speak("Good afternoon Sir")

    elif(hour>=16 and  hour<=19):
        speak("Good evening Sir")
    else:
        speak("Good night Sir")
    speak("Myself August!,Your personal voice assistant. How may i help you.")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self) :
        self.taskexecution()
        
    def acceptcommands(self):   # module for accepting voice input from user and recognizes with google_recognize. and converting into text string.
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening---")
            r.pause_threshold=0.5
            r.energy_threshold= 1
            audio=r.listen(source,timeout=1,phrase_time_limit=5)

        try:
            print("recognizing")
            query=r.recognize_google(audio, language="en-in")
            # speak(query)
            print(f"user said: {query}")
        except Exception as error:
            # speak("can't recognize..please speak again...")
            return "NONE"
        return query

    def taskexecution(self):
        
        if __name__ == "__main__":
            speak("What is your password")
            password = self.acceptcommands().lower()
            if(password == "august" or password=="August"):
                wish()
                while True:
                    self.query = self.acceptcommands().lower()

                    # logic building for tasks
                    if "open notepad" in self.query:             # to open notepad
                        npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                        os.startfile(npath)

                    elif "open command prompt" in self.query or "open cmd" in self.query:    # to open cmd
                        os.system("start cmd")

                    elif "open" in self.query:
                        from Dictapp import openappweb
                        openappweb(self.query)
                    elif "close" in self.query:
                        from Dictapp import closeappweb
                        closeappweb(self.query)

                    elif "hide files" in self.query:
                        speak("do you want to hide the file")
                        a=self.acceptcommands().lower()
                        if(a=="yes" or a=="Yes"):
                            os.system("attrib +h /s secret")
                            speak("Your files and folders are hidden now")
                        else :
                            break

                    elif "show hidden files" in self.query:             
                        speak("do you want to show hidden file")
                        a=self.acceptcommands().lower() 
                        if(a=="yes" or a=="Yes"):
                            os.system("attrib -h /s secret")
                            speak("Your files and folders are not hidden now")
                        else :
                            break

                    elif "read pdf" in self.query:
                        pdf_reader()

                    elif "news" in self.query:
                        from NewsRead import latestnews
                        latestnews()

                    elif "temperature" in self.query:
                        try:
                            res = app_id.query(self.query)
                            print(next(res.results).text)
                            speak(next(res.results).text)
                        except:
                            print("Internet connection error")

                    elif "click my photo" in self.query:             # to open camera
                        click_pic()
                    
                    elif "I am tired" in self.query:
                        speak("Sir I will play song to cheer you up")
                        music_dir = "C:\\Users\\saksh\\OneDrive\\Desktop\\newfinalaugust\\music"
                        songs = os.listdir(music_dir)
                        rd = random.choice(songs)
                        os.startfile(os.path.join(music_dir,rd))



                    elif "what is my location" in self.query:
                        speak("Wait sir , Let me check")
                        try:
                            ipAdd = requests.get('https://api.ipify.org').text
                            print(ipAdd)
                            url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                            geo_requests = requests.get(url)
                            geo_data = geo_requests.json()
                            city = geo_data['city']
                            country = geo_data['country']
                            speak(f"Sir I am not sure, but I think we are in {city} city of {country} country")
                        except Exception as e:
                            speak("Sorry I could'nt get your Location")

                    elif "shutdown system" in self.query:
                        speak("are you sure you want to shutdown")
                        cm=self.acceptcommands().lower()          
                        if (cm == "yes" or cm=="Yes"):
                            os.system("shutdown /s /t 1") 
                        else:
                            break                 

                    elif "whatsapp" in self.query:
                         from Whatsapp import sendMessage
                         sendMessage()
                    
                    elif "ip address" in self.query:                               # for Ip address
                        ip=get('https://api.ipify.org').text
                        speak(f"Your IP address is {ip}"+"For your convenience I will print on console")
                        print("ip="+ip)

                    elif "switch tab" in self.query:
                        user32.keybd_event(0x12, 0, 0, 0) #Alt
                        sleep(1)
                        user32.keybd_event(0x09, 0, 0, 0) #Tab
                        sleep(1)

                    elif "play song on youtube" in self.query :                     # to play song on youtube
                        speak("What should I play on Youtube")
                        cm=self.acceptcommands().lower()
                        kit.playonyt(cm)


                    elif "pause" in self.query:
                            pyautogui.press("k")
                            speak("video paused")

                    elif "Fullscreen" in self.query:
                            pyautogui.press("f")

                    elif "play" in self.query:
                        pyautogui.press("k")
                        speak("video played")

                    elif "mute" in self.query:
                        pyautogui.press("m")
                        speak("video muted")
                    
                    elif "ummute" in self.query:
                        pyautogui.press("m")
                        speak("video unmuted")

                    elif "increase volume" in self.query:
                        speak("Turning volume up,sir")
                        volumeup()

                    elif "decrease volume" in self.query:
                        
                        speak("Turning volume down, sir")
                        volumedown()

                    elif "screenshot" in self.query:
                         import pyautogui #pip install pyautogui
                         im = pyautogui.screenshot()
                         im.save("ss.jpg")

                    elif "send email" in self.query:
                        try:
                            to = "reciver mails address"
                            speak("What should I send sir")
                            content = self.acceptcommands().lower()
                            sendEmail(to , content)
                            speak("Email sent successfully")
                        except Exception as e:
                            speak("Could not send email due to network issue")

                    elif ("How much power Left" or "battery") in self.query:
                        battery = psutil.sensors_battery()
                        percentage = battery.percent
                        speak(f"sir our system have {percentage} percent battery")


                    elif "system volume up" in self.query:
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")

                    elif "system volume mute" in self.query:
                        pyautogui.press("volumemute")

                    elif "system volume down" in self.query:
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")


                    elif "wikipedia" in self.query: 
                                                        # to open wikipedia
                        self.query = self.query.replace("wikipedia", "")
                        results = wikipedia.summary(self.query, sentences= 4)
                        speak("According to wikipedia ")
                        speak(results)
                        speak("For your convenience I will print on console")
                        print(results)

                    elif "open youtube" in self.query:                              # to open yotube
                        webbrowser.open("www.youtube.com")

                    elif "close notepad" in self.query:
                        speak("closing Notepad")
                        os.system("taskill /f /im WINWORD.exe")                            # to close function

                    elif "open facebook" in self.query:                             # to open facebook
                        webbrowser.open("www.facebook.com")
                    
                    elif "open instagram" in self.query:                             # to open instgram
                        webbrowser.open("www.instagram.com")
                    
                    elif "open twitter" in self.query:                             # to open twitter
                        webbrowser.open("www.twitter.com")
                    
                    elif "open facebook" in self.query:                             # to open facebook
                        webbrowser.open("www.facebook.com")
                    
                    # elif "tell me a joke":
                    #     speak("Joke for the day is")
                    #     joke = pyjokes.get_joke()
                    #     speak(joke)
                    #     speak("for your convinece I will print on screen")
                    #     print(joke)

                    elif "open google" in self.query:                               # to open google 
                        speak("Sir, What should I search on Google")
                        cm = self.acceptcommands().lower()
                        webbrowser.open(f"{cm}") 

                    elif "internet speed" in self.query:
                        speak("Checking internet speed")
                        wifi  = speedtest.Speedtest()
                        upload_net = wifi.upload()        #Megabyte = 1024*1024 Bytes
                        download_net = wifi.download()
                        print("Wifi Upload Speed is", upload_net)
                        print("Wifi download speed is ",download_net)
                        speak(f"Wifi download speed is {download_net}")
                        speak(f"Wifi Upload speed is {upload_net}")
            

                    elif "alarm" in self.query:
                        speak("Enter the time")
                        time=input("Enter time :") 
                        while True:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            
                            if strTime == time:
                                speak("alarm buzzed")
                                playsound("MV27TES-alarm.mp3")
                                speak("Alarm closed")
                            elif strTime>time :
                                break
                                

                    elif "calculate" in self.query:
                        from Calculatenumbers import WolfRamAlpha
                        from Calculatenumbers import Calc
                        self.query = self.query.replace("calculate","")
                        self.query = self.query.replace("jarvis","")
                        Calc(self.query)


                    elif "the time" in self.query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                        speak(f"Sir, the time is {strTime}")


                    elif "send text message" in self.query:
                        # speak("what should I say Sir")
                        # cm = self.acceptcommands()
                        import os
                        from twilio.rest import Client
                        # Set environment variables for your credentials
                        # Read more at http://twil.io/secure
                        account_sid = "ACec3f160521136a4f6537f171581ca8bf"
                        auth_token = os.environ["75b561def6fb6e3d8921686a6d20d926"]
                        client = Client(account_sid, auth_token)
                        message = client.messages.create(
                        body="Hello from Twilio",
                        from_="+16205428347",
                        to="+919021731925"
                        )
                        print(message.sid)

                    elif "no thanks" in self.query:                                 # to close august
                        speak("thank you for using me . have a good day")
                        sys.exit()
                    speak("Do you have any other work")    
            else:
                 speak("Your password is worng Try again")     

                 self.taskexecution()
startEXecution = MainThread()


class Main(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.ui = Ui_augustui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\saksh\\OneDrive\\Desktop\\newfinalaugust\\ezgif.com-resize.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startEXecution.start()

    def terminalPrint(self,text):
        self.ui.terminalOutputBox.appendPlainText(text)
    def manualCodeFromTerminal(self):
        cmd = self.ui.terminalInputBox.text()
        if cmd:
            self.ui.terminalInputBox.clear()
            self.ui.terminalOutputBox.appendPlainText(f"You just typed >>{cmd}")

            if cmd == 'exit':
                august.close()
            elif cmd=='help':
                self.terminalPrint("I can perform various operation like: ")
            else:
                pass
        else:
            pass

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(label_time)
        self.ui.textBrowser_3.setText(label_date)
        
app = QApplication(sys.argv)
august = Main()
august.show()
exit(app.exec_())

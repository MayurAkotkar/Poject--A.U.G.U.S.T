import requests
import json
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=48341b96a99545f5a068f9b7a1358dbf",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=48341b96a99545f5a068f9b7a1358dbf",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=48341b96a99545f5a068f9b7a1358dbf",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=48341b96a99545f5a068f9b7a1358dbf",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=48341b96a99545f5a068f9b7a1358dbf",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=48341b96a99545f5a068f9b7a1358dbf"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    
    field = takeCommand().lower()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        speak("Do you want to continue, Say Yes to continue or No to stop ")
        a = takeCommand().lower()
        if str(a) == ("yes" or "Yes"):
            pass
        elif str(a) == ("no" or "NO"):
            break
        
    speak("thats all")
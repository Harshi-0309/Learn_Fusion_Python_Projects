import speech_recognition as sr
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyttsx3
import requests
import time

class VoiceBot:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.running = True
        self.commands = {
            "search": self.search_google,
            "open youtube": self.open_youtube,
            "news": self.get_news,
            "weather": self.get_weather
        }
        self.listen_on_mic()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_on_mic(self):
        while self.running:
            try:
                with sr.Microphone() as source:
                    print("Listening for commands...")
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(f"Command received: {command}")
                    self.handle_command(command)

            except sr.UnknownValueError:
                self.speak("Sorry, I did not catch that. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def handle_command(self, command):
        if "exit" in command:
            self.speak("Exiting...")
            self.running = False
        else:
            for key in self.commands:
                if command.startswith(key):
                    self.commands[key](command)
                    return
            self.speak("Command not recognized.")

    def search_google(self, command):
        search_query = command.split('search ')[-1]
        self.speak(f"Searching for {search_query}")
        chrome_service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.get(f"https://www.google.com/search?q={search_query}")
        time.sleep(10)  # Keeps the browser open for 10 seconds
        driver.quit()

    def open_youtube(self, command):
        if "for" in command:
            search_query = command.split('for ')[-1]
            self.speak(f"Searching YouTube for {search_query}")
            chrome_service = Service(ChromeDriverManager().install())
            chrome_options = Options()
            driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            driver.get(f"https://www.youtube.com/results?search_query={search_query}")
        else:
            self.speak("Opening YouTube")
            chrome_service = Service(ChromeDriverManager().install())
            chrome_options = Options()
            driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            driver.get("https://www.youtube.com")
        
        time.sleep(10)  # Keeps the browser open for 10 seconds
        driver.quit()

    def get_news(self, command):
        self.speak("Fetching the latest news")
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY")
        if response.status_code == 200:
            news = response.json()
            for article in news["articles"][:5]:
                self.speak(article["title"])
        else:
            self.speak("Sorry, I couldn't fetch the news.")

    def get_weather(self, command):
        self.speak("Fetching the weather report")
        response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m")
        if response.status_code == 200:
            weather = response.json()
            self.speak(f"The current temperature is {weather['hourly']['temperature_2m'][0]} degrees.")
        else:
            self.speak("Sorry, I couldn't fetch the weather.")

if __name__ == "__main__":
    VoiceBot()


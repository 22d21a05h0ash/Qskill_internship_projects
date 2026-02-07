import speech_recognition as sr
import pyttsx3
import requests
import datetime


engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)   # DEBUG
    engine.say(text)
    engine.runAndWait()


listener = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

        try:
            command = listener.recognize_google(audio)
            print("You said:", command)
            return command.lower().strip()

        except Exception as e:
            print("Speech Error:", e)
            speak("Sorry, I did not understand")
            return ""


def get_weather(city):

    api_key = "b477f5d8e62678be909c73e5ea27578b"   # PUT KEY

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        r = requests.get(url)

        print("API Status:", r.status_code)
        print("API Response:", r.text)   # DEBUG

        data = r.json()

        if r.status_code == 200:

            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]

            speak(f"The temperature in {city} is {temp} degree Celsius")
            speak(f"The weather is {desc}")

        else:
            speak("Weather service error")

    except Exception as e:
        print("Request Error:", e)
        speak("Network problem")


def extract_city(command):

    words = ["in", "of", "at", "for"]

    for w in words:
        if w in command:
            return command.split(w)[-1].strip()

    return None


def run_assistant():

    speak("Hello, I am your assistant. How can I help you?")

    while True:

        command = listen()

        print("Command received:", command)   # DEBUG

        if command == "":
            continue


        # TIME
        if "time" in command:

            time = datetime.datetime.now().strftime("%I:%M %p")
            speak("Current time is " + time)


        # DATE
        elif "date" in command:

            date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + date)


        # WEATHER
        elif "weather" in command:

            city = extract_city(command)

            if city:
                speak(f"Checking weather in {city}")
                get_weather(city)

            else:
                speak("Tell me the city name")
                city = listen()
                get_weather(city)


        # HELLO
        elif "hello" in command or "hi" in command:

            speak("Hello! How are you?")


        # EXIT
        elif "exit" in command or "stop" in command:

            speak("Goodbye")
            break


        # DEFAULT
        else:
            speak("Sorry, I did not understand that")


if __name__ == "__main__":
    run_assistant()

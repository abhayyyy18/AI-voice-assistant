import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser
import smtplib
import wikipedia
import openai
import os

# Set up OpenAI API key
openai.api_key = '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'

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to convert speech to text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return None

# Function to get the current date and time
def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%A, %d %B %Y %I:%M %p")

# Function to get the weather using OpenWeatherMap API (you need an API key)
def get_weather(city):
    api_key = 'b961b79568d1484d7724c7e98e9311d0'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        weather_info = data["weather"][0]["description"]
        return f"The weather in {city} is currently {weather_info}."
    else:
        return "City not found. Please check the city name."

# Function to open websites
def open_website(url):
    webbrowser.open(url)

# Function to open file explorer
def open_file_explorer():
    os.system('explorer')

def open_command_prompt():
    os.system('start /min cmd')

def shutdown():
    os.system('shutdown /s /t 1')  # Shutdown the system

def restart():
    os.system('shutdown /r /t 1')  # Restart the system

def logoff():
    os.system('shutdown /l')   # Log off the current user


# Function to send an email (you need to enable "Less secure app access" in your Gmail account)
def send_email(receiver, subject, body):
    # Your email credentials
    sender_email = 'abhaychouksey1818@gmail.com'
    sender_password = 'Abbusalem18'

    # Set up the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Compose the email
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    server.sendmail(sender_email, receiver, message)
    server.quit()

# Function to search Wikipedia
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found. Can you be more specific? {e}"


def open_control_panel():
    os.system('control')  # Open Control Panel

# Function to ask OpenAI API
def ask_openai(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip() 


def open_application(application_name):
    # Dictionary mapping application names to their corresponding executable paths
    application_paths = {
        'chrome': r'C:\Users\ASUS\Desktop\apps\Abhay - Chrome.lnk',  # Example path for Google Chrome on Windows
        'spotify': r'C:\Users\ASUS\AppData\Local\Microsoft\WindowsApps\Spotify.exe',  # Example path for Spotify on Windows
        'code': r'C:\Users\ASUS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk',
        # Example path for Visual Studio Code on Windows
        'pycharm': r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.3.4.lnk',
        # Example path for PyCharm on Windows
        'winword': r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk',
        # Example path for Microsoft Word on Windows
        'excel': r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk'
        # Example path for Microsoft Excel on Windows
    }

    # Check if the application name exists in the dictionary
    if application_name in application_paths:
        # Get the corresponding executable path
        executable_path = application_paths[application_name]
        # Open the application
        os.system(f'"{executable_path}"')
    else:
        print(f"Error: Application '{application_name}' not found.")

# Main function to handle user queries
def main():
    speak("Hello! Friday here How can I help you today?")
    print("Hello! Friday here How can I help you today?")
    while True:
        user_input = listen()

        if user_input:
            if 'open google chrome' in user_input:
                open_application('chrome')
            elif 'open spotify' in user_input:
                open_application('spotify')
            elif 'open vs code' in user_input:
                open_application('code')
            elif 'open pycharm' in user_input:
                open_application('pycharm')
            elif 'open word' in user_input:
                open_application('winword')
            elif 'open excel' in user_input:
                open_application('excel')
            elif 'open file explorer' in user_input:
                open_file_explorer()
            elif 'open command prompt' in user_input:
                open_command_prompt()
            elif 'open control panel' in user_input:
                open_control_panel()
            elif 'shutdown' in user_input:
                shutdown()
            elif 'restart' in user_input:
                restart()
            elif 'logoff' in user_input:
                logoff()
            elif "tell me the date and time" in user_input:
                speak(get_date_time())
                print(get_date_time())
            elif "how is the weather" in user_input:
                speak("Sure, please tell me the city.")
                city = listen()
                if city:
                    speak(get_weather(city))
                    print(get_weather(city))
            elif "open website" in user_input:
                speak("Sure, please tell me the website.")
                website = listen()
                if website:
                    open_website(f"https://www.{website}.com")
            elif "send email" in user_input:
                speak("Sure, please tell me the recipient's email address.")
                receiver_email = listen()
                speak("What should be the subject of the email?")
                email_subject = listen()
                speak("What should be the body of the email?")
                email_body = listen()
                if receiver_email and email_subject and email_body:
                    send_email(receiver_email, email_subject, email_body)
                    speak("Email sent successfully.")
            elif "search wikipedia" in user_input:
                speak("Sure, please tell me what you want to search on Wikipedia.")
                wiki_query = listen()
                if wiki_query:
                    speak(search_wikipedia(wiki_query))
                    print(search_wikipedia(wiki_query))
            elif "ask open ai" in user_input:
                speak("Sure, please ask your question.")
                user_question = listen()
                if user_question:
                    speak(ask_openai(user_question))
            elif "exit" in user_input or "bye" in user_input:
                speak("Goodbye! Have a great day.")
                break
            else:
                speak("I'm sorry, I didn't understand that. Can you please repeat?")
        else:
            speak("I'm sorry, I couldn't hear you. Can you please repeat?")

if __name__ == "__main__":
    main()
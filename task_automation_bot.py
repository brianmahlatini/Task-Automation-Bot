# Install dependencies for Colab
!pip install -q requests


import json
import datetime
import requests
import time


WEATHER_API_KEY = 'demo'  
WEATHER_CITY = 'London'

# In-memory to-do list
todo_list = []

# Greeting based on time
def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 17:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Weather fetching
def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={WEATHER_CITY}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The current weather in {WEATHER_CITY} is {description} with a temperature of {temp}°C."
    else:
        return "Unable to fetch weather."

# Add a task
def add_task(task):
    todo_list.append(task)
    return f"Task '{task}' added."

# Show tasks
def show_tasks():
    if not todo_list:
        return "Your to-do list is empty."
    return "Here are your tasks:\n" + "\n".join([f"- {task}" for task in todo_list])

# Simple news fetcher (static sample)
def get_news():
    sample_news = [
        "OpenAI releases new AI model.",
        "Python remains the most popular programming language.",
        "Global tech salaries are rising in 2025."
    ]
    return "Today's top news:\n" + "\n".join(f"- {news}" for news in sample_news)

# Main bot loop
def run_bot():
    print("🤖 Task Automation Bot")
    print("Type 'exit' to stop.\n")
    print(get_greeting())

    while True:
        command = input("🧑 You: ").lower()

        if command in ['exit', 'quit']:
            print("🤖 Bot: Goodbye! Automation session ended.")
            break
        elif "weather" in command:
            print("🤖 Bot:", get_weather())
        elif "add task" in command:
            task = command.replace("add task", "").strip()
            print("🤖 Bot:", add_task(task))
        elif "show tasks" in command or "to-do" in command:
            print("🤖 Bot:", show_tasks())
        elif "news" in command:
            print("🤖 Bot:", get_news())
        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Bot: The current time is {now}")
        else:
            print("🤖 Bot: Sorry, I didn’t understand that. Try asking about weather, news, or tasks.")

# Run the bot
run_bot()

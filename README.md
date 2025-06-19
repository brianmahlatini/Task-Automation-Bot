Task Automation Bot
Overview
This Python-based Task Automation Bot provides a simple command-line interface to automate everyday productivity tasks such as managing a to-do list, fetching news headlines, checking the current time, and retrieving weather information for a specified city. It showcases skills in Python programming, API integration, and user interaction design.
Features
•	Add tasks to your to-do list with simple commands
•	Display your current to-do list
•	Fetch sample news headlines
•	Get the current local time
•	Retrieve current weather information for a specified city
•	Intelligent greetings based on the time of day
•	User-friendly command-line interface with continuous interaction until exit
Technologies Used
•	Python 3.x
•	Standard libraries: datetime, json, time
•	External libraries: requests for API calls (weather data)
How to Run
1.	Install required packages:
bash
CopyEdit
pip install requests  
2.	Run the Python script:
bash
CopyEdit
python task_automation_bot.py  
3.	Use the following commands during the interactive session:
o	add task <task description> — Adds a task to your to-do list
o	show tasks or to-do — Displays all your tasks
o	news — Shows sample news headlines
o	time — Shows current time
o	weather — Fetches the current weather for London (default)
o	exit or quit — Ends the session
Example Interaction
yaml
CopyEdit
🤖 Task Automation Bot  
Type 'exit' to stop.

Good afternoon!  
You: add task finish report  
Bot: Task 'finish report' added.

You: show tasks  
Bot: Here are your tasks:  
- finish report

You: news  
Bot: Today's top news:  
- OpenAI releases new AI model.  
- Python remains the most popular programming language.  
- Global tech salaries are rising in 2025.

You: time  
Bot: The current time is 14:30:45

You: weather  
Bot: The current weather in London is light rain with a temperature of 12°C.

You: exit  
Bot: Goodbye! Automation session ended.
Customization
You can replace the default city for weather by changing the WEATHER_CITY variable in the script.
To use real-time news, you can integrate a news API by modifying the get_news() function.
About Me
I am a mid-level software developer with over 3 years of experience specializing in Python development, automation, and AI-driven solutions. I have a strong background in designing and implementing practical applications that solve real-world problems efficiently.
This project demonstrates my hands-on skills in building interactive command-line tools, integrating external APIs, and applying software engineering best practices. I continuously seek to improve my craft by learning new technologies and delivering clean, maintainable code.
I am passionate about leveraging automation and AI to enhance productivity and user experiences.


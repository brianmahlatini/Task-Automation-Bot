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



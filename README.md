# README: Flight Search Script

## Description
This Python script automates flight searches using the Skyscanner API. It schedules and executes daily search tasks, collecting information about itineraries and prices, and stores the data in a CSV file.

## Requirements
- Python 3
- Libraries: requests, json, pandas, datetime, schedule, time, python-dotenv
- Skyscanner API Key

## Setup
1. Install the necessary dependencies using pip:
   `pip install requests pandas python-dotenv schedule`
2. Create a `.env` file in the project root and add your Skyscanner API key:
   `API_KEY='YourApiKeyHere'`

## Usage
To run the script, use the command in the terminal:
`python script_name.py`
The script will schedule and execute the flight search task every hour, saving the results in a CSV file in the `bases` folder.

## Script Structure
- `create_search()`: Makes a request to the Skyscanner API to search for flights.
- `scheduled_task()`: Generates search dates, iterates over different airport combinations, and performs the flight search.

## Additional Notes
- Replace `script_name.py` with the actual name of your script file.
- The script uses the `schedule` library to schedule tasks. Adjust the frequency as necessary.
- The Skyscanner API key must be obtained by registering on the Skyscanner developers portal.
# Extracting Stock Data Using a Python Library

#Using the yfinance Library to Extract Stock Data

import os
import json
import requests
from yfinance import Ticker

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
file_name = "amd.json"

# Step 1: Verify current working directory
print("Current Directory:", os.getcwd())

# Step 2: Check if the file exists
if 'amd.json' not in os.listdir():
    print("File 'amd.json' not found. Downloading it...")
    # Download the JSON file
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
else:
    print("File 'amd.json' is already in the directory.")

# Step 3: Load the JSON file
try:
    with open('amd.json') as json_file:
        amd_info = json.load(json_file)
        print("JSON file loaded successfully.")
except FileNotFoundError:
    print("The file 'amd.json' was not found. Please check the download step.")
    amd_info = None
except Exception as e:
    print(f"An error occurred while loading the file: {e}")
    amd_info = None

# Step 4: Work with the data if it was successfully loaded
if amd_info:
    print("Type of amd_info:", type(amd_info))
    country = amd_info.get('country', 'Country information not found')
    print("Country:", country)
    sector = amd_info.get('sector', 'Sector information not found')
    print("Sector:", sector)
    
    amd = Ticker('AMD')  # Create the Ticker object for AMD
    amd_history = amd.history(period="max")  # Get historical data with period set to max

    # Find the Volume traded on the first day
    first_day_volume = amd_history['Volume'].iloc[0]  # Access the first row's Volume
    print("Volume traded on the first day:", first_day_volume)
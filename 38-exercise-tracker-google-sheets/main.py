from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

# nutritionix
APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "female"
WEIGHT_KG = 60
HEIGHT_CM = 180
AGE = 26

# sheety
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
GOOGLE_SHEET_NAME = "workout"

# get exercises and calories from prompt
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
exercise_config = {
    "query": input("Tell which exercise you did today?: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_config, headers=exercise_headers)
response.raise_for_status()
result = response.json()

today = datetime.now()

# save data from each exercise to workouts table
for exercise in result['exercises']:
    sheety_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    sheety_body = {
        GOOGLE_SHEET_NAME: {
            'date': today.strftime('%d/%m/%Y'),
            'time': today.strftime('%X'),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=sheety_headers)
    response.raise_for_status()

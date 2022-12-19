import requests
from datetime import datetime


time_now = datetime.now().strftime("%d/%m/%Y")
today_date = datetime.now().strftime("%X")

with open("Proj37-WorkoutTracking/api_key.txt") as key_file:
    API_KEY = key_file.read()
with open("Proj37-WorkoutTracking/app_id.txt") as id_file:
    APP_ID = id_file.read()
    
NUTRITIONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

SHEETY_API_ENDPOINT = "https://api.sheety.co/0c9fb1d95f7034c772d814c56ed52d78/workoutTracking/workouts"
    
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
}

response_0 = requests.post(url=NUTRITIONIX_API_ENDPOINT, headers=headers, json=parameters)
response_0.raise_for_status()
data = response_0.json()
print(data)

for exercise in data.get("exercises"):
    workout = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise.get("name").title(),
            "duration": exercise.get("duration_min"),
            "calories": exercise.get("nf_calories"),
        },
    }

    response_1 = requests.post(url=SHEETY_API_ENDPOINT, json=workout)
    response_1.raise_for_status()

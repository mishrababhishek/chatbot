import requests
from datetime import datetime
import pytz

def get_user_timezone():
    try:
        response = requests.get('https://ipapi.co/timezone/')
        return response.text.strip()
    except requests.exceptions.RequestException:
        return None

def get_updated_string(original_string: str):
    user_timezone = get_user_timezone()

    if user_timezone:
        current_time = datetime.now(pytz.timezone(user_timezone)).time()
        hour = current_time.hour

        if hour < 12:
            greeting = "Good morning!"
        elif hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"

        updated_string = ""
        temp = original_string.split(" ")
        updated_string = f"{temp[0]} {greeting} " + " ".join(temp[1:])
        return updated_string
    else:
        return "Unable to determine your timezone."
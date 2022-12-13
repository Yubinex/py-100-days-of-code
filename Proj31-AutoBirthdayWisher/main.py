import pandas as pd
from datetime import datetime
import random
import smtplib


MY_EMAIL = "j.hauck1999@gmail.com"
PASSWORD = "srvbrxidcrzxtftb"


today = datetime.now()
today_tuple = (today.month, today.day)

birthdays_data = pd.read_csv("Proj31-AutoBirthdayWisher/birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (
    index, data_row) in birthdays_data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"Proj31-AutoBirthdayWisher/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file=file_path) as f:
        letter = f.read()
        letter = letter.replace(
            "[NAME]", birthdays_dict[today_tuple].get("name"))

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_dict[today_tuple].get("email"),
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )
    print(f"Mail successfully send to {birthdays_dict[today_tuple].get('name')} - {birthdays_dict[today_tuple].get('email')}")

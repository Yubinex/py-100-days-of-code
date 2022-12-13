import smtplib
import datetime as dt
from random import choice

# get quotes
with open("Proj31-AutoBirthdayWisher/quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()

# variables
my_email = "j.hauck1999@gmail.com"
password = "srvbrxidcrzxtftb"

# get current day
now = dt.datetime.now()
day = now.weekday()

if day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="janhauck99@gmail.com",
            msg=f"Subject:Motivational Quote\n\n{choice(quotes)}"
        )

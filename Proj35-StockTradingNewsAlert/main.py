import requests
import datetime as dt
import smtplib

# script version
VERSION = 1.1

# date constants
if dt.datetime.today().hour < 7:
    TODAY_DATE = dt.date.today() - dt.timedelta(days=1)
else:
    TODAY_DATE = dt.date.today()
YESTERDAY_DATE = TODAY_DATE - dt.timedelta(days=1)
BEFORE_YESTERDAY_DATE = YESTERDAY_DATE - dt.timedelta(days=1)

# desired stock name
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API endpoints and keys
STOCK_ENDPOINT = "http://api.marketstack.com/v1/eod"
with open(file="Proj35-StockTradingNewsAlert/stock_api_key.txt") as stock_key_file:
    STOCK_API_KEY = stock_key_file.read()
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
with open(file="Proj35-StockTradingNewsAlert/news_api_key.txt") as news_key_file:
    NEWS_API_KEY = news_key_file.read()

MY_EMAIL = "yubinex.dev@gmail.com"
with open(file="Proj35-StockTradingNewsAlert/email_password.txt") as email_passwd_file:
    PASSWORD = email_passwd_file.read()

RECIPIENTS = [
    "janhauck99@gmail.com",
    #"uwehauck@gmail.com",
    #"sibylle@familie-hauck.de",
    #"marchauck04@gmail.com",
]

# getting data from stock api
stock_params = {
    "access_key": STOCK_API_KEY,
    "symbols": STOCK_NAME,
    "date_from": BEFORE_YESTERDAY_DATE,
    "date_to": YESTERDAY_DATE,
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
stock_data_list = [value for (key, value) in stock_data.items()][1]

# get yesterday's closing price
yesterday_data = stock_data_list[0]
yesterday_high = yesterday_data["high"]
yesterday_low = yesterday_data["low"]
yesterday_closing = yesterday_data["close"]
# get before yesterday's closing price
before_yesterday_data = stock_data_list[1]
before_yesterday_high = before_yesterday_data["high"]
before_yesterday_low = before_yesterday_data["low"]
before_yesterday_closing = before_yesterday_data["close"]
# get the difference between the two days
pos_diff = abs(yesterday_closing - before_yesterday_closing)
# get precentage difference
diff_percent = (pos_diff / yesterday_closing) * 100
# print("Get News") if diff_percent is greater than 5
# TODO: Set 3 back to 5 after testing
if diff_percent > 3:
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME,
        "from": TODAY_DATE,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_data_list = [value for (key, value) in news_data.items()][2][0:3]

    # compose mail
    pos_or_neg = ""
    if before_yesterday_closing < yesterday_closing:
        pos_or_neg = "+"
    elif before_yesterday_closing == yesterday_closing:
        pos_or_neg = "="
    else:
        pos_or_neg = "-"
        
    difference = f"{pos_or_neg}{round(pos_diff, 2)}({pos_or_neg}{round(diff_percent, 2)}%)"
    difference_detail = f"{pos_or_neg}{pos_diff}({pos_or_neg}{diff_percent}%)"
    
    mail_subject = f"Subject:{COMPANY_NAME} [{STOCK_NAME}] {difference}\n\n"
    mail_content = f"""
Exact difference: {difference_detail}

Stock Information:

HIGHEST:
    [{BEFORE_YESTERDAY_DATE}] - ${round(before_yesterday_high, 2)}
    [{YESTERDAY_DATE}] - ${round(yesterday_high, 2)}

LOWEST:
    [{BEFORE_YESTERDAY_DATE}] - ${round(before_yesterday_low, 2)}
    [{YESTERDAY_DATE}] - ${round(yesterday_low, 2)}
    
CLOSING:
    [{BEFORE_YESTERDAY_DATE}] - ${round(before_yesterday_closing, 2)}
    [{YESTERDAY_DATE}] - ${round(yesterday_closing, 2)}
    
'{COMPANY_NAME}' Top 3 News Articles [{TODAY_DATE}]


[1] {news_data_list[0].get("title")}
    by {news_data_list[0].get("author")}
    
Article Description: 
{news_data_list[0].get("description")}

Link to article: {news_data_list[0].get("url")}
    
    
[2] {news_data_list[1].get("title")}
    by {news_data_list[1].get("author")}
    
Article Description:
{news_data_list[1].get("description")}

Link to article: {news_data_list[1].get("url")}
    
    
[3] {news_data_list[2].get("title")}
    by {news_data_list[2].get("author")}
    
Article Description:
{news_data_list[2].get("description")}

Link to article: {news_data_list[2].get("url")}


@yubinex - automatically generated email via StockTradingNewsAlert(v{VERSION})
"""
    mail = mail_subject + mail_content

    for email in RECIPIENTS:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=mail,
            )
        print(f"Email successfully sent to '{email}'")

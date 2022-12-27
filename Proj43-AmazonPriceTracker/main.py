import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URL = "https://www.amazon.de/-/en/dp/B09WDKQLGQ/?coliid=I2KOG928S7NSOL&colid=2XFYYKPSV8LP0&ref_=lv_ov_lig_dp_it&th=1"
HIGHEST_PRICE = 250

MY_EMAIL = "yubinex.dev@gmail.com"
with open(file="Proj35-StockTradingNewsAlert/email_password.txt") as email_passwd_file:
    PASSWORD = email_passwd_file.read()
TO_ADDR = "janhauck99@gmail.com"

headers = {
    "User-Agent": "Defined",
}
response = requests.get(PRODUCT_URL, headers=headers)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
product_title = soup.find(name="span", id="productTitle").text.strip()
product_price = soup.find(name="span", class_="a-offscreen")
pure_product_price = product_price.text[1:]

if float(pure_product_price) < HIGHEST_PRICE:
    mail_subj = f"Subject:Amazon Price Alert\n\n"
    mail_cont = f"""
TRACKED PRODUCT:
{product_title}

Price dropped below EUR {HIGHEST_PRICE} -> Current price: EUR {pure_product_price}
"""
    mail = mail_subj + mail_cont

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDR,
            msg=mail,
        )
    print(f"Email successfully sent to '{TO_ADDR}'")

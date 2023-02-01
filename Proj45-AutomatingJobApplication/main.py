from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

with open("Proj45-AutomatingJobApplication\\secret.txt") as file:
    lines = file.readlines()
ACCOUNT_EMAIL = lines[0].strip()
ACCOUNT_PASSWORD = lines[1].strip()

chrome_driver_path = "D:\\Tools\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
 # type: ignore
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# Sign In
sign_in_btn = driver.find_element(By.CSS_SELECTOR, '.nav__button-secondary.btn-md.btn-secondary-emphasis')
sign_in_btn.click()

session_key = driver.find_element(By.NAME, "session_key")
session_password = driver.find_element(By.NAME, "session_password")
session_key.send_keys(ACCOUNT_EMAIL)
session_password.send_keys(ACCOUNT_PASSWORD)

login_form = driver.find_element(By.CLASS_NAME, "login__form")
login_form.submit()

# Wait for a few seconds - let page load
time.sleep(3)

# Get results
main_list = driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container")
results = main_list.find_elements(By.TAG_NAME, "a")
print(len(results))
for res in results:
    print("--------------------")
    print(res.text)
    print(res.get_attribute("href"))

time.sleep(60)

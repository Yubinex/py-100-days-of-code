from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# I DON'T WANT TO TWEET AT PROVIDER
# PROMISED_DOWN = 150
# PROMISED_UP = 10
CHROME_DRIVER_PATH = "D:\\Tools\\chromedriver_win32\\chromedriver.exe"
with open("Proj45-AutomatingJobApplication\\secret.txt") as file:
    lines = file.readlines()
TWITTER_EMAIL = lines[0].strip()
TWITTER_PASSWORD = lines[1].strip()


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.up = 0
        self.down = 0
        self.ping = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        cookies = self.driver.find_element(
            By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        cookies.click()

        go = self.driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go.click()

        for i in range(60, 0, -1):
            print(f"Waiting {i}...", end='\r')
            time.sleep(1)
        print("Continuing...", end='\r')
        
        self.up = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.ping = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[2]/span').text

        print(f"UP -> {self.up}")
        print(f"DOWN -> {self.down}")
        print(f"PING -> {self.ping}")

    def tweet_at_provider(self):
        print("NOT IMPLEMENTED!")
    
    def tweet_internet_speed(self):
        self.driver.get("https://twitter.com/")
        time.sleep(1000)


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_internet_speed()

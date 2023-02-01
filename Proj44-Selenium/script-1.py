from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "D:\\Tools\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
search_symbol = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[2]/div/a").click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()

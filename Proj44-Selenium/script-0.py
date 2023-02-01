from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\\Tools\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_descs = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "desc": event_descs[n].text,
    }
print(events)


# Close/Quit Browser
# driver.close()
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome browser open after program finishes
google_options = webdriver.ChromeOptions()
google_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=google_options)

driver.get("https://www.python.org/")
anchor_list = driver.find_elements(By.CSS_SELECTOR, value="div.event-widget div ul li a")
time_list = driver.find_elements(By.CSS_SELECTOR, value="div.event-widget div ul li time")
events = {}
for n in range(len(time_list)):
    events[n] = {
        "time": time_list[n].text,
        "name": anchor_list[n].text
    }
print(events)

driver.close()

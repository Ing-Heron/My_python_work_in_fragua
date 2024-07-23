from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome browser open after program finishes
google_options = webdriver.ChromeOptions()
google_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=google_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.CLASS_NAME, value="top")
last_name = driver.find_element(By.CLASS_NAME, value="middle")
email_address = driver.find_element(By.CLASS_NAME, value="bottom")
button = driver.find_element(By.TAG_NAME, value="button")

first_name.send_keys("hola")
last_name.send_keys("hello")
email_address.send_keys("hola@gmail.com")
button.click()

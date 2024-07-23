from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome browser open after program finishes
google_options = webdriver.ChromeOptions()
google_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=google_options)

# Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS selectors
number_of_articles = driver.find_element(By.CSS_SELECTOR, value="div#articlecount a")

# click
# number_of_articles.click()
search_button = driver.find_element(By.CSS_SELECTOR, value="div#p-search a")
search_button.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)

# driver.close()

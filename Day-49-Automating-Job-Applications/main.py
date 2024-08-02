from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

URL = ("https://www.linkedin.com/jobs/search/?currentJobId=468695816&f_AL=true&keywords=python&"
       "location=M%C3%A9xico&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
EMAIL_USER = "heronsanchez26@gmail.com"
PASSWORD = "miracomomerio"

google_options = webdriver.ChromeOptions()
google_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=google_options)
driver.get(URL)
login_a = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
login_a.click()
email = driver.find_element(By.XPATH, value='//*[@id="username"]')
password = driver.find_element(By.XPATH, value='//*[@id="password"]')
sleep(2)
button_login = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
email.send_keys(EMAIL_USER)
password.send_keys(PASSWORD)
button_login.click()

jobs_ul = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div/ul')
jobs_list = jobs_ul.find_elements(By.CLASS_NAME, value='job-card-container__link')

for job_to_save in range(0, 3):
    jobs_list[job_to_save].click()
    sleep(2)
    save_button = driver.find_element(By.CLASS_NAME, value='jobs-save-button')
    save_button.click()
    sleep(2)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://dev2.halightdev.com/")
driver.maximize_window()
driver.find_element(By.ID, "email").send_keys("Saraswat")
driver.find_element(By.ID, "password").send_keys("Lion@123")
driver.find_element(By.CSS_SELECTOR, "button[id ='login-card-submit-button']").click()
time.sleep(10)  # keeps the browser open for 10 seconds

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("https://dev2.halightdev.com/")
driver.find_element(By.LINK_TEXT, "Sign Up").click()
fake = Faker() #To generate random names
random_firstname = fake.first_name()
random_lastname = fake.last_name()
random_email = random_firstname + random_lastname + "@gmail.com" #concatenating with domain name

driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys(random_firstname)
print(random_firstname + " " + random_lastname)
print(random_email)
driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys(random_lastname)
driver.find_element(By.CSS_SELECTOR, "#email").send_keys(random_email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Lion@123")

dropdown = Select(driver.find_element(By.NAME, "country"))
dropdown.select_by_value("IN")

division = Select(driver.find_element(By.NAME, "hierarchy"))
division.select_by_visible_text("SJ DIV")

usertype = Select(driver.find_element(By.NAME, "userType"))
usertype.select_by_visible_text("SJ User Type")
time.sleep(5)
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element(By.ID, "email")
password = browser.find_element(By.ID, "pass")
submit = browser.find_element(By.NAME, "login")
username.send_keys("YOUR NAME")
password.send_keys("HOW WAS YOUR DAY")
# Step 4) Click Login
submit.click()
wait = WebDriverWait(browser, 5)
page_title = browser.title
# assert page_title == "Facebook"
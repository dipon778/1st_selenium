import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#
#
os.environ['PATH'] += "/usr/local/bin/chromedriver"
driver = webdriver.Chrome()


#driver.get("https://phptravels.com/demo/")
driver.get("https://phptravels.net/login/")
# driver.implicitly_wait(10)
# my_e = driver.find_element(By.XPATH, "/html/body/div[2]/main/section[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/a")
# my_e.click()

email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")

email.send_keys('user@phptravels.com')
password.send_keys("demouser")

loginbtn = driver.find_element(By.XPATH, '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button')
loginbtn.click()
# driver.get("https://www.python.org")
# print(driver.title)
# search_bar = driver.find_element(By.NAME, "q")
# search_bar.clear()
# search_bar.send_keys(" python install ubuntu")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)

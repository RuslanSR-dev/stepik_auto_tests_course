from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://sdesk.qa.eft-pos.ru/requests"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    login = driver.find_element(By.XPATH, "//input[contains(@id, 'login')]")
    login.send_keys("salakhov.rr")
    password = driver.find_element(By.XPATH, "//input[contains(@id, 'password')]")
    password.send_keys("yQ7u67cKL@_2w")
    button = driver.find_element(By.XPATH, "")



    input = driver.find_element(By.XPATH, "//div[contains(text(), 'Новая заявка')]").click()

finally:
    time.sleep(5)
    driver.close()
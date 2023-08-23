from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    verify = browser.find_element(By.XPATH, "//button[contains(@id, 'verify')]")
    verify.click()
    message = browser.find_element(By.XPATH, "//div[contains(text(), 'Verification was successful!')]")

    assert 'successful' in message.text
finally:
    browser.close()

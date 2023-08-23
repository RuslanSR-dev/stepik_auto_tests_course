from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
file_name = "../text.txt"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//input[contains(@name, 'firstname')]")
    first_name.send_keys("Ruslan")

    last_name = browser.find_element(By.XPATH, "//input[contains(@name, 'lastname')]")
    last_name.send_keys("Salakhov")

    email = browser.find_element(By.XPATH, "//input[contains(@name, 'email')]")
    email.send_keys("Ruslan")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.XPATH, "//input[contains(@type, 'file')]")
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

finally:
    time.sleep(5)
    browser.close()

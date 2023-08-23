from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[contains(@class, 'trollface')]")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.XPATH, "//span[contains(@id, 'input_value')]")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, "//input[@id='answer']")
    input.send_keys(y)

    submit = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    submit.click()

finally:
    time.sleep(5)
    browser.close()

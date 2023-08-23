from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, "//input[@id='answer']")
    input.send_keys(y)

    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn')]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    check_box = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']")
    check_box.click()

    radiobutton = browser.find_element(By.XPATH, "//label[@for='robotsRule']")
    radiobutton.click()

    button.click()

finally:
    time.sleep(5)
    browser.close()

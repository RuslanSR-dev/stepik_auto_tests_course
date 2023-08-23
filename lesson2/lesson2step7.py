from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element(By.ID, "treasure")
    x = box.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(7)
    browser.quit()

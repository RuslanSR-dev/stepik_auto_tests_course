from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from lesson1_step1.Function import calc

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    check_box = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check_box.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()



finally:
    time.sleep(5)
    browser.quit()

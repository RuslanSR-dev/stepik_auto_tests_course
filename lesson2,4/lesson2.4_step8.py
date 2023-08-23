from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[contains(@id, 'price')]"), "$100"))

    button = browser.find_element(By.XPATH, "//button[contains(@id, 'book')]")
    button.click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    element = browser.find_element(By.XPATH, "// span[contains( @ id, 'input_value')]")
    x = element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, "//input[contains(@id, 'answer')]")
    input.send_keys(y)

    submit = browser.find_element(By.XPATH, "//button[contains(@id, 'solve')]")
    submit.click()

finally:
    time.sleep(12)
    browser.close()

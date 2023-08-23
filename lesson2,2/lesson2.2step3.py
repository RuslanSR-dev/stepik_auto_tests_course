from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    def summ(x, y):
        num = int(x) + int(y)
        return str(num)


    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "num1")
    num1 = input1.text
    num1 = int(num1)

    input2 = browser.find_element(By.ID, "num2")
    num2 = input2.text
    num2 = int(num2)

    num3 = summ(num1, num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(num3)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(7)
    browser.close()

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    var = browser.find_element(By.XPATH, "//button[contains(@id, 'button')]")


finally:
    browser.close()

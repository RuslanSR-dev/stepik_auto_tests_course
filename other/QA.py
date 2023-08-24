from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://sdesk.qa.eft-pos.ru/login"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    login = browser.find_element(By.XPATH, "//input[@id='login']")
    login.send_keys("salakhov.rr")

    password = browser.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("yQ7u67cKL@_2w")

    button = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary ladda-button']")
    button.click()

    browser.implicitly_wait(5)
    new_request = browser.find_element(By.XPATH, "//*[contains(@class, 'k-grid-column-menu k-grid-filter')]")
    new_request.click()
    #
    # input5 = browser.find_element(By.XPATH, "//a/i[@class='ion ion-ios-log-out text-danger']/..")
    # input5.click()

    #fghkl
finally:
    time.sleep(15)
    browser.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://sdesk.qa.eft-pos.ru/login"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element(By.XPATH, "//input[@id='login']")
    input.send_keys("salakhov.rr")

    input2 = browser.find_element(By.XPATH, "//input[@id='password']")
    input2.send_keys("yQ7u67cKL@_2w")

    input3 = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary ladda-button']")
    input3.click()

    input4 = browser.find_element(By.XPATH, "//div[@class='demo-navbar-user nav-item dropdown']/a")
    input4.click()

    input5 = browser.find_element(By.XPATH, "//a/i[@class='ion ion-ios-log-out text-danger']/..")
    input5.click()

finally:
    time.sleep(10)
    browser.close()

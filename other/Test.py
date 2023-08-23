from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://www.xml2selenium.com/'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text = browser.find_element(By.XPATH, "//div[@class='list-4']/ul[count(li)=4]")
    print(string(text))

finally:
    time.sleep(3)
    browser.close()

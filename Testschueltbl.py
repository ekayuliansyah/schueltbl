from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("https://zzzscore.com/1to50/en/")

try:
    driver.implicitly_wait(3)
    for i in range(1,51):
        xpath1 = "//div[contains(@style, 'opacity: 1;') and .//text()[normalize-space() = '"+str(i)+"']]"
        driver.find_element(By.XPATH,xpath1).click()
finally:
    time.sleep(5)
    driver.quit()

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")
wait = WebDriverWait(driver, 10)
search = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'gLFyf')))
search.send_keys("Selenium Python")


searchBox = wait.until( EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))

for s in searchBox:
    print(s.text)

searchBox[1].click()

sleep(5)

driver.quit()
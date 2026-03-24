from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://automationexercise.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]/child::li[4]').click()

driver.find_element(By.NAME, "name").send_keys("Niteesh")

driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys('temp1122@gmail.com')

btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='signup-button']")))
btn.click()

driver.find_element(By.ID, "id_gender1").click()
n=driver.find_element(By.ID, "newsletter")
n.click()


off = driver.find_element(By.ID, "optin")
off.click()

time.sleep(5)
driver.quit()
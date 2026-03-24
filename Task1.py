from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.amazon.in/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
sleep(3)
assert "Amazon" in driver.title, "verification failed"
assert "https://www.amazon.in/" in driver.current_url, 'verification failed'

drop = driver.find_element(By.ID, "searchDropdownBox")
select = Select(drop)
select.select_by_visible_text("Books")

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("harry potter",Keys.ENTER)

product = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/span')))
for i in product:
    print(i.text)

product[0].click()
sleep(10)
driver.quit()
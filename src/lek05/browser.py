import time 
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FireFoxService
# for driver and managing 
from selenium.webdriver.common.by import By 
# for filtering
from selenium.webdriver.support import expected_conditions as EC 
# for wait conditions
from selenium.webdriver.support.ui import WebDriverWait
# Wait condition (using EC and By)
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox() # depending on the browser
driver.get("https://demoqa.com/buttons")
find = driver.find_element(By.ID, "doubleClickBtn")
print(find.text)
action = ActionChains(driver)
action.double_click(on_element=find)
time.sleep(2)
find2 = driver.find_element(By.ID, "rightClickBtn")
action.context_click(on_element=find2)
action.perform()
time.sleep(2)
# find3 = driver.find_element(By.ID, "J1xtR")
# action.click(on_element=find3)
# action.perform()
# find an array of elements by CSS_SELECTOR type
find3 = driver.find_elements(By.CSS_SELECTOR, ".btn.btn-primary")
find3[2].click()

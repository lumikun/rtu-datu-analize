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

url = "https://demoqa.com/automation-practice-form"

driver = webdriver.Firefox() # depending on the browser
driver.get(url)
found = driver.find_element(By.ID, "firstName")
found.send_keys("John")
found = driver.find_element(By.ID, "lastName")
found.send_keys("Doe")
found = driver.find_element(By.ID, "userEmail")
found.send_keys("John.Doe@example.com")
found = driver.find_element(By.ID, "userNumber")
found.send_keys("1234567890")
found = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[3]" )
found.click()
driver.execute_script("window.scrollBy(0, 500);")
found = driver.find_element(By.ID, "submit")
found.click()
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "closeLargeModal")))
found = driver.find_element(By.ID, "closeLargeModal")
found.click()

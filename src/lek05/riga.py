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

url = "https://riga.lv"

driver = webdriver.Firefox() # depending on the browser
driver.get(url)
time.sleep(1)
try:
    found = driver.find_element(By.PARTIAL_LINK_TEXT, "Aizvērt")
    print(found.text)
    found.click()
except:
    pass
found = driver.find_element(By.CLASS_NAME, "cookie-accept-all")
found.click()
found = driver.find_element(By.CLASS_NAME, "search-link")
found.click()
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "edit-search")))
found = driver.find_element(By.ID, "edit-search")
found.send_keys("Dokum")
found = driver.find_element(By.ID, "search-header-button")
found.click()
found = driver.find_element(By.CLASS_NAME, "criteria-filters-btn")
found.click()
found = driver.find_element(By.CSS_SELECTOR, "label[for='search-content-type']")
found.click()
found = driver.find_element(By.CLASS_NAME, "autocomplete-input")
found.send_keys("Vak")
#found = driver.find_element(By.PARTIAL_LINK_TEXT, "Vakance")
found = driver.find_element(By.CSS_SELECTOR, "div.js-form-item:nth-child(19) > label:nth-child(2)")
found.click()
found = driver.find_element(By.ID, "search-view-button-custom")
found.click()


# Tālāk var ar beautifulsoup visu parsot utt.
kods = driver.page_source
print(kods)
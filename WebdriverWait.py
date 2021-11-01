from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://google.com")

wait = WebDriverWait(driver, 10)
title = wait.until(ec.title_is('Google'))
print(driver.title)
search = wait.until(ec.presence_of_element_located((By.XPATH, "//input[@type='tee']")))
search.send_keys("cricbuzz.com")
driver.quit()
# now we can access any element of web page without taking a wait because
# if title is visible then surely there will be all elements are present


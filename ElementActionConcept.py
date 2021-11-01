import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://classic.crmpro.com/index.html")
time.sleep(3)
action = ActionChains(driver)

username = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
login_button = driver.find_element(By.XPATH, "//input[@type='submit']" )

action.send_keys_to_element(username, "kiranshidruk@gmail.com")
action.send_keys_to_element(password, "kiranshidruk")
action.click(login_button).perform()
time.sleep(3)
driver.quit()

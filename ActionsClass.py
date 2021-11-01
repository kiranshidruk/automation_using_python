import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

time.sleep(3)
action = ActionChains(driver)

'''move to element method'''

cat_ele = driver.find_element(By.CSS_SELECTOR, 'nav button span')
action.move_to_element(cat_ele).perform()

time.sleep(3)
dev_ele = driver.find_element(By.LINK_TEXT, 'Development')
action.move_to_element(dev_ele).perform()

time.sleep(3)
web_dev_ele = driver.find_element(By.LINK_TEXT, 'Web Development')
action.move_to_element(web_dev_ele).perform()

time.sleep(3)
Django_ele = driver.find_element(By.LINK_TEXT, 'Django')
action.click(Django_ele).perform()

time.sleep(5)
driver.quit()





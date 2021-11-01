import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
# dynamic wait
# will wait till 10
# implicity wait wait will bw applied for the all elements
# global wait
# find element
# find elements
# only applied to web elements
# not for non web elements like title, url , alerts
driver.get("https://github.com/login")

driver.find_element(By.ID, "login_field").send_keys("kingship")

driver.find_element(By.ID, 'password').send_keys("kiran")

driver.quit()

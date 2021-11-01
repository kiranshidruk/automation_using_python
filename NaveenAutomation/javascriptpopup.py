import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
time.sleep(3)
# action = ActionChains(driver)

driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)

alert1 = driver.switch_to.alert
print(alert1.text)
alert1.accept()

driver.switch_to.default_content()
time.sleep(3)
driver.quit()





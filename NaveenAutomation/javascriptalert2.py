import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(3)

# driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
# driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(3)
alert = driver.switch_to.alert
driver.sw
print(alert.text)
alert.send_keys("I am testing jsPrompt")
alert.accept()
# alert.dismiss()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(3)
driver.quit()

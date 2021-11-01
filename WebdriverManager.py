import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


browsername= "chrome"

if browsername == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browsername == "firefox":
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print("please enter the correct driver")
    raise Exception("entered wrong browser name")


time.sleep(5)
driver.get("https://github.com/")

driver.find_element(By.NAME, 'user_email').send_keys("kiranshidruk27@gmail.com")
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

print(driver.title)
time.sleep(5)
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
'''Auth POP UP'''


# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# time.sleep(3)
# driver.quit()

'''file upload pop up'''


driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
time.sleep(3)

driver.find_element(By.NAME, 'upfile').send_keys("/home/kiran/Downloads/download.jpeg")
driver.find_element(By.XPATH, '//input[@type="submit"]').click()
time.sleep(3)
driver.quit()




import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.amazon.in/")


'''diff methods like back, forward, refresh '''
# driver.find_element(By.LINK_TEXT, 'Best Sellers').click()
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
# driver.quit()

'''cookies'''
print(driver.get_cookies())
driver.add_cookie({"domain": ".amazon.in", "name": "kiran", "value": "working on selenium"})
print(driver.get_cookies())
time.sleep(3)
driver.quit()

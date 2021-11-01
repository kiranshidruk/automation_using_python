import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://www.londonfreelance.org/courses/frames/index.html")
time.sleep(3)

# driver.switch_to.frame('main')
# driver.switch_to.frame(2)
ti_ele = driver.find_element(By.NAME, 'main')
driver.switch_to.frame(ti_ele)
title_ele= driver.find_element(By.XPATH, "//body[@background='top.gif']")

print(title_ele.text)
time.sleep(3)

driver.switch_to.default_content()
# driver.quit()




print("Edited By Kiran")
print("edited by  Development1")
x


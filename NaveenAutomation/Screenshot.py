import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.amazon.in/")

driver.get_screenshot_as_file("amazonhome.jpg")
driver.get_
S= lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name("body").screenshot("amazonfullscrnshot.jpg")
time.sleep(3)
driver.quit()

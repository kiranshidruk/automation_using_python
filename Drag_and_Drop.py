import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

time.sleep(3)
action = ActionChains(driver)


draggable = driver.find_element(By.ID, 'draggable')
droppable = driver.find_element(By.ID, 'droppable')

# action.drag_and_drop(draggable, droppable).perform()

action.click_and_hold(draggable).move_to_element(droppable).release().perform()

time.sleep(3)

driver.quit()


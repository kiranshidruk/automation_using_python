import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(3)
action = ActionChains(driver)


right_click = driver.find_element(By.CSS_SELECTOR, 'p span')
action.context_click(right_click).perform()
time.sleep(3)

list_right = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon span')

for ele in list_right:
    print(ele.text)
    if ele.text == 'Copy':
        ele.click()
        break

time.sleep(3)
driver.quit()



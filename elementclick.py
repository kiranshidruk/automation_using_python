import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://github.com/kiranshidruk/JenkinsProject/settings/hooks")

wait = WebDriverWait(driver, 10)
sign_in = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Sign up')))
print(sign_in.text)
sign_in.click()

first_name = wait.until(ec.visibility_of_element_located((By.ID, 'email')))
first_name.send_keys('Kiran Shidruk')

# multiple_ele = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR , "")))
# print(multiple_ele)
# for ele in multiple_ele:
#     print(ele)

'''similarly we can use'''

# wait.until(ec.frame_to_be_available_and_switch_to_it(By.ID, 'djsi'))
wait.until(ec.url_contains('github'))

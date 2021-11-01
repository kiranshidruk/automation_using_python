import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.orangehrm.com/hris-hr-software-demo/")


print("edited by kiran")




def select_dropdown(ele, value):
    select = Select(ele)
    select.select_by_visible_text(value)

#  *By using Select option *



# select_con = driver.find_element(By.ID, 'Form_submitForm_Country')
# select = Select(select_con)
# select.select_by_visible_text('India')
# select.select_by_value('France')
# select.select_by_index(2)
# print(select.is_multiple)
# select_dropdown(select_con, 'India')
# select_op_list = select.options
# for ele in select_op_list:
#     print(ele.text)
#     if ele.text == 'Colombia':
#         ele.click()
#         break



# Without using select (using XPATH)

select_ele_list = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Country"]/option')

for ele in select_ele_list:
    print(ele.text)
    if ele.text == 'India':
        ele.click()
        break

time.sleep(5)
driver.quit()



# if you have multidrop use CSS selector = span.something_name
#  if multidrop down case arraises pass all the values in list and put logic to select in function

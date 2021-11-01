import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="/home/kiran/Downloads/Selenium/chromedriver/chromedriver")
driver.get("http://www.google.com/")
driver.implicitly_wait(5)
print(driver.title)
driver.find_element(By.NAME, "q").send_keys("naveen automationlabs")
time.sleep(5)

optionslist = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")
# for id we can use css selector by using #usename --> By.CSS_SELECTOR, "#username"
# for class we can use css selector by using .(Dot)class_name(unique if have many classes
#  for having many classes use css selector by using tag_name.class1.class2.class3
#  xpath we can use for linktest as //a[text()="Click Here"]
# for going parent to child use XPATh as //div[@id="sfi"]/label for other example //form[div[@id="sdi"]/div[1]/label
# for going parent to child use CSS SELECTOR div[id="dufn"] label
for data in optionslist:
    print(data.text)
    if data.text == 'naveen automationlabs youtube':
        data.click()
        break;

time.sleep(5)
driver.quit()



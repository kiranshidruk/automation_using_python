import time
from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Chrome

# Firstway
# options = Options()
# options.add_argument("--allow-running-insecure-content")
# options.add_argument("--ignore-certificate-errors")

#Secondway
# desired_capabilities = DesiredCapabilities().CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True

#ThirdWay
# options = Options()
# options.set_capability('acceptInsecureCerts', True)

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

# Firefox

#firstway
# profile = webdriver.FirefoxProfile()
# profile.accept_untrusted_certs = True

desired_capability = DesiredCapabilities.FIREFOX.copy()
desired_capability['acceptInsecureCerts'] = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), desired_capabilities=desired_capability)
driver.get("https://expired.badssl.com/")

# print(driver.find_element(By.TAG_NAME, "h1").text)
print(driver.find_element_by_tag_name("h1").text)

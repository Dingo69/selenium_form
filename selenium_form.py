from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in

# TEST_DATA = {
#             'username': 'tomsmith',
#             'password': 'SuperSecretPassword!',
#             'Logged in': 'Welcome to the Secure Area. When you are done click logout below.'
# }
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/login")
# time.sleep(2)
#
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys(TEST_DATA['username'])
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#password").send_keys(TEST_DATA['password'])
# time.sleep(1)
# driver.find_element_by_css_selector("#login > button > i").click()
#
# assert driver.find_element(By.CLASS_NAME, "subheader").text == TEST_DATA['Logged in']
# time.sleep(2)
# driver.quit()


# 2. Login with invalid creds and check validation error
#
# TEST_DATA = {
#             'username': 'tomsmitty',
#             'password': 'SuperPuperSecretPassword!',
# }
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/login")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys(TEST_DATA['username'])
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#password").send_keys(TEST_DATA['password'])
# time.sleep(1)
# driver.find_element_by_css_selector("#login > button > i").click()
#
# assert 'Your username is invalid' or 'Your password is invalid' in browser.page_source
# time.sleep(2)
# driver.quit()


# 3. Logout from app and assert you successfully logged out

# TEST_DATA = {
#             'username': 'tomsmith',
#             'password': 'SuperSecretPassword!',
#             'Logged in': 'Welcome to the Secure Area. When you are done click logout below.',
# }
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/login")
# time.sleep(2)
#
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys(TEST_DATA['username'])
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#password").send_keys(TEST_DATA['password'])
# time.sleep(1)
# driver.find_element_by_css_selector("#login > button > i").click()
#
# assert driver.find_element(By.CLASS_NAME, "subheader").text == TEST_DATA['Logged in']
# time.sleep(3)
#
# driver.find_element_by_css_selector("#content > div > a").click()
# time.sleep(3)
# assert 'You logged out of the secure area' in driver.page_source
# time.sleep(3)
#
# driver.quit()
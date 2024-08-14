'''import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)
MyAcc_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(2)")
MyAcc_btn.click()
#Register
Email = driver.find_element_by_id("reg_email")
Email.send_keys("martynova.ev1991@gmail.com")
Password = driver.find_element_by_id("reg_password")
Password.send_keys("martynovaev1991@")
Register = driver.find_element_by_tag_name("[name='register']")
Register.click()'''




import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
MyAcc_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(2)")
MyAcc_btn.click()
#Login
Email = driver.find_element_by_id("username")
Email.send_keys("martynova.ev1991@gmail.com")
Password = driver.find_element_by_id("password")
Password.send_keys("martynovaev1991@")
Login = driver.find_element_by_tag_name("[name='login']")
Login.click()
Logout = WebDriverWait(driver, 25).until(
EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))
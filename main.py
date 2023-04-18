# @Author : ligenm
# #File : main
# @time : 2023/4/13 10:10
import time
from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://sso-test.i4px.com/login?service=https://daily-idms2-manager.i4px.com//cas'
driver.get(url)

# 设置浏览器窗口大小
# driver.set_window_size(1600,1200)
driver.maximize_window()
driver.find_element_by_id('login-type-i').click()
driver.find_element_by_id('username').send_keys('S9638')
driver.find_element_by_id('passwordOrg').send_keys('lgm#90621')
driver.find_element_by_id('signbtn').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div[@class='ant-select-selection__rendered']").click()
driver.find_element_by_xpath("//ul[@role='listbox']/li[7]").click()
driver.find_element_by_class_name("ant-btn").click()
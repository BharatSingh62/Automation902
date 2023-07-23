# from selenium import webdriver
# import time
# import pytest


# def test_login_LP1(Setup):
#     driver=Setup
#     driver.find_element_by_id("user-name").send_keys("standard_user")
#     driver.find_element_by_id("password").send_keys("secret_sauce")
#     driver.find_element_by_id("login-button").click()
#     actual_text= driver.find_element_by_xpath("//span[contains(text(),'Products')]").text
#     expected_text="Products"
#     assert actual_text==expected_text


# # def test_login_LP2(Setup):    
# #     driver=Setup
# #     driver.find_element_by_id("user-name").send_keys("standard_userXX")
# #     driver.find_element_by_id("password").send_keys("secret_sauce1_XX")
# #     driver.find_element_by_id("login-button").click()
# #     actual_text=driver.find_element_by_css_selector("div.login_container div.login_wrapper div.login_wrapper-inner div.form_column div.login-box form:nth-child(1) > div.error-message-container.error:nth-child(3)").text
# #     expected_text="Epic sadface: Username and password do not match any user in this service"
# #     assert actual_text==expected_text

# # def test_login_LP3(): 
# #     driver.find_element_by_id("user-name").send_keys("locked_out_user")
# #     driver.find_element_by_id("password").send_keys("secret_sauce")
# #     driver.find_element_by_id("login-button").click()
# #     actual_text=driver.find_element_by_css_selector("div.login_container div.login_wrapper div.login_wrapper-inner div.form_column div.login-box form:nth-child(1) div.error-message-container.error:nth-child(3) > h3:nth-child(1)").text
# #     expected_text="Epic sadface: Sorry, this user has been locked out."
# #     assert actual_text==expected_text

# # def test_login_LP4():
# #     driver=Setup
# #     driver.find_element_by_id("user-name").send_keys("locked_out_user")
# #     driver.find_element_by_id("password").send_keys("secret_sauce")
# #     driver.find_element_by_id("login-button").click()
# #     actual_text=driver.find_element_by_css_selector("div.login_container div.login_wrapper div.login_wrapper-inner div.form_column div.login-box form:nth-child(1) div.error-message-container.error:nth-child(3) > h3:nth-child(1)").text
# #     expected_text="Epic sadface: Sorry, this user has been locked out."
# #     assert actual_text==expected_text

# # def test_login_LP5():
# #     driver=Setup
# #     driver.find_element_by_id("user-name12").send_keys("locked_out_user")
# #     driver.find_element_by_id("password").send_keys("secret_sauce")
# #     driver.find_element_by_id("login-button").click()
# #     actual_text=driver.find_element_by_css_selector("div.login_container div.login_wrapper div.login_wrapper-inner div.form_column div.login-box form:nth-child(1) div.error-message-container.error:nth-child(3) > h3:nth-child(1)").text
# #     expected_text="Epic sadface:"
# #     assert actual_text==expected_text

# # def test_login_LP5(Setup):
# #     driver=Setup
# #     driver.find_element_by_id("user-name").send_keys("locked_out_user")
# #     driver.find_element_by_id("password").send_keys("secret_sauce")
# #     driver.find_element_by_id("login-button").click()
# #     actual_text=driver.find_element_by_css_selector("div.login_container div.login_wrapper div.login_wrapper-inner div.form_column div.login-box form:nth-child(1) div.error-message-container.error:nth-child(3) > h3:nth-child(1)").text
# #     expected_text="Epic sadface: Sorry, this user has been locked out."
# #     assert actual_text==expected_text
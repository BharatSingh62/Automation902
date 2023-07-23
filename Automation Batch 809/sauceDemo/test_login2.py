from selenium import webdriver
import time
import pytest

class Test_Login2_testCase:
    def test_login_01(self,Setup):
        self.driver=Setup
        driver=self.driver
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()
        

    def test_login_02(self,Setup):
        self.driver=Setup
        driver=self.driver
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()
    
    def test_login_03(self,Setup):
        self.driver=Setup
        driver=self.driver
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()

    def test_login_04(self,Setup):
        self.driver=Setup
        driver=self.driver
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()
    



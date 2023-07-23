from selenium import webdriver
import pytest


@pytest.fixture()
def Setup():
    print("Setup is launched")
    driver_path="Drivers\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()
    url="https://www.saucedemo.com/"
    driver.get(url)
    yield driver
    driver.quit()


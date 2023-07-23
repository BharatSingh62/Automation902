from selenium import webdriver
import time
import pytest

@pytest.mark.xfail
def test_Product_P_P1(Setup):
    driver=Setup
    print("test_Product_PP2")

@pytest.mark.skip
def test_Product_PP2_(Setup):    
    driver=Setup
    print("test_Product_PP2") 
    assert 15==15

@pytest.mark.Regression
def test_Product_PP3_P1(Setup):
    driver=Setup
    print("test_Product_PP2")
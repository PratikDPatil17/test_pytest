#from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver

import time

class TestGoogleSearch:
    @pytest.fixture
    def setUptearDown(self):
        #setUp method
        global driver
        options = Options()
        #driver =Service("D:\Python_Tutorials\Python_Unit_Testing_test\pytest_test\chromedriver.exe")
        #browser = webdriver.Chrome(service=driver)
        driver = webdriver.Chrome(executable_path='P:/StudyWork/Python Programs/PythonProg/Web_scrapping/Naukari_WebScrapping/chromedriver')
        #driver = webdriver.Chrome(executable_path="P:\Python_Tutorials\Python_Unit_Testing_test\pytest_test\chromedriver.exe")

        driver.get("https://www.google.co.in/")
        driver.maximize_window()

        yield
        #tearDown method
        time.sleep(10)
        browser.close()

    def test_googleSearch(self, setUptearDown):
        driver.find_element_by_name('q').send_keys("Sachin Tendulkar")
        #driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("Sachin Tendulkar")

        time.sleep(4)
        driver.find_element_by_name('btnk').click()
        driver.find_element_by_class_name('LC20lb').click()

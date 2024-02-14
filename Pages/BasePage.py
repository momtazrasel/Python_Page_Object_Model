import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService


class BaseClass(unittest.TestCase):
    driver: WebDriver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService())
        cls.driver.maximize_window()
        cls.driver.get("https://www.demoblaze.com/")
        print("Test Started")

    @classmethod
    def tearDown(cls):
        time.sleep(2)
        cls.driver.quit()

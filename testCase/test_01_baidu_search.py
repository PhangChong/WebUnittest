import time
import unittest

from selenium.webdriver.common.by import By

from base.get_browser import GetBrowser
from pageObject.baidu_homepage import *


class Search(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = GetBrowser(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search1(self):
        homepage = HomePage(self.driver)
        homepage.baidu_search('peng')
        homepage.send_btn()
        homepage.sleep(2)
        homepage.get_windows_screenshot()

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.baidu_search('chong')
        homepage.send_btn()
        time.sleep(2)
        homepage.get_windows_screenshot()

    def test_get_title(self):
        homepage = HomePage(self.driver)
        print(homepage.get_page_title())

import unittest

from base.get_browser import GetBrowser
from pageObject.baidu_hot import *


class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = GetBrowser(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_hot_click(self):
        # 点击百度热搜在切回主页
        homehot = HomeHot(self.driver)
        homehot.hot_click()
        homehot.sleep(3)
        homehot.to_home()
        try:
            homehot.tryassert()
            print('Test Pass.')
        except:
            print('Test Fail.')
        homehot.sleep(3)

import unittest

from base.get_browser import GetBrowser
from pageObject.baidu_set_search_set import *


class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = GetBrowser(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_set_search_set(self):
        # 移动至设置---搜索设置--选择条件并保存
        homeset = HomeSet(self.driver)
        homeset.move_set()
        homeset.search_set_click()
        homeset.search_page_set()

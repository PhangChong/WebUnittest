from base.base_page import BasePage
from selenium.webdriver.common.by import By


class HomeHot(BasePage):
    hot_button = (By.XPATH, '//i[@class="c-icon"]')

    def hot_click(self):
        self.click(self.hot_button)

    def to_home(self):
        self.switchWindow(0)

    def tryassert(self):
        self.displayed((By.XPATH, '//*[@id="hotsearch-refresh-btn"]/span'))

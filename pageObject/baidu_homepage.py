from base.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    input_box = (By.ID, 'kw')
    search_btn = (By.ID, 'su')

    def baidu_search(self, text):
        self.sendkeys(self.input_box, text)

    def send_btn(self):
        self.click(self.search_btn)

from base.base_page import BasePage
from selenium.webdriver.common.by import By


class HomeSet(BasePage):
    set_btn = (By.ID, 's-usersetting-top')
    search_set_button = (By.LINK_TEXT, '搜索设置')

    def move_set(self):
        self.mouseMoveTo(self.set_btn)

    def search_set_click(self):
        self.click(self.search_set_button)

    def search_page_set(self):
        self.click((By.XPATH, '//li[@data-tabid="advanced"]'))
        self.click((By.XPATH, '//li[@data-tabid="general"]'))
        self.click((By.ID, 's1_2'))
        self.click((By.ID, 'sh_2'))
        self.click((By.XPATH, '//*[@id="se-setting-7"]/a[2]'))
        self.sleep(1)
        self.accept()

import time
import os.path
from tool.logs import Logs

logger = Logs(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        # 浏览器退出操作
        self.driver.quit()

    def forward(self):
        # 浏览器前进操作
        self.driver.forward()
        logger.info("当前页面进行前进操作.")

    def back(self):
        # 浏览器后退操作
        self.driver.back()
        logger.info("当前页面进行后退操作.")

    def close(self):
        # 点击关闭当前窗口
        try:
            self.driver.close()
            logger.info("关闭当前页面.")
        except Exception as e:
            logger.error("关闭浏览器失败，错误: %s" % repr(e))

    def element(self, selector):
        # 定位元素方法
        self.driver.find_element(selector[0], selector[1])

    def sendkeys(self, selector, text):
        # 输入文本框
        el = self.driver.find_element(selector[0], selector[1])
        el.clear()
        try:
            el.send_keys(text)
            logger.info("在输入框中输入了'%s'" % text)
        except NameError as e:
            logger.error("在输入框中输入 %s 失败" % e)
            self.get_windows_screenshot()

    def clear(self, selector):
        # 清除文本框
        el = self.driver.find_element(selector[0], selector[1])
        try:
            el.clear()
            logger.info("清除输入框中的文本.")
        except NameError as e:
            logger.error("无法在输入框中清除 %s" % e)
            self.get_windows_screenshot()

    def click(self, selector):
        # 点击元素
        el = self.driver.find_element(selector[0], selector[1])
        try:
            et = el.text
            el.click()
            logger.info("点击了元素 '%s' ." % et)
        except NameError as e:
            # if e==NameError:
            #     e=NameError
            # else:
            #     e=repr(e)
            logger.error("未能点击到元素 %s " % e)

    def text(self, selector):
        # 获取文本
        el = self.driver.find_element(selector[0], selector[1])
        try:
            et = el.text
            logger.info("得到的文本为 %s" % et)
        except NameError as e:
            logger.error("无法得到文本 %s" % e)
            self.get_windows_screenshot()

    def displayed(self, selector):
        # 秀
        return self.driver.find_element(selector[0], selector[1]).is_displayed

    def get_page_title(self):
        # 获得网页标题
        logger.info("当前的页面标题是 %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("休眠 %d 秒" % seconds)

    # -----------------------------------------------------------
    # -----------------------------------------------------------
    # ----------------------------------------------------------
    def get_windows_screenshot(self):
        # 当前窗口截图
        file_path = os.path.dirname(os.path.abspath('.')) + r'/screenshots/'
        # file_path=直接保存到项目根目录的.\Screenshots下
        sysTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
        try:
            self.driver.get_screenshot_as_file(file_path + sysTime + '.png')
            logger.info("已截图并保存到文件夹: /screenshots")

        except NameError as e:
            logger.error("截图失败! %s" % e)
            self.get_windows_screenshot()

    def switchWindow(self, num):
        # 切换窗口
        self.driver.switch_to.window(self.driver.window_handles[num])
        logger.info("已切换至第{}页窗口".format(num + 1))

    def mouseMoveTo(self, selector):
        # 鼠标移动
        from selenium.webdriver.common.action_chains import ActionChains
        element = self.driver.find_element(selector[0], selector[1])
        ActionChains(self.driver).move_to_element(element).perform()
        logger.info("已移动到了元素 '%s' ." % element.text)

    def accept(self):
        self.driver.switch_to.alert.accept()
        logger.info("已在弹窗点击确定.")

    def dismiss(self):
        self.driver.switch_to.alert.dismiss()
        logger.info("已在弹窗点击取消.")

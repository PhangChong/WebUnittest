import os.path
from selenium import webdriver
from tool.logs import Logs
from tool.read_conf import ReadIni

logger = Logs(logger="GetBrowser").getlog()


class GetBrowser(object):

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        # 获取配置文件属性
        browser = ReadIni().get("browserType", "browserName")
        logger.info("选择了 %s browser." % browser)
        url = ReadIni().get("testURL", "URL")
        logger.info("测试网址为: %s" % url)

        testsystem = ReadIni().get("testSystem", "tSystem")
        dir = os.path.dirname(os.path.abspath('.'))
        if testsystem == '1':
            testsystemOS = 'MacOs'
            chrome_driver_path = dir + '/adrivers/chromedriver'
            firefox_driver_path = dir + '/adrivers/geckodriver'
            ie_driver_path = dir + '/adrivers/xxxx'
        else:
            chrome_driver_path = dir + '/adrivers/chromedriver.exe'
            firefox_driver_path = dir + '/adrivers/geckodriver.exe'
            ie_driver_path = dir + '/adrivers/IEDriverServer.exe'
            testsystemOS = 'Windows'
        logger.info("选择系统为: %s" % testsystemOS)
        try:
            if browser == 'Firefox':
                driver = webdriver.Firefox(firefox_driver_path)
                logger.info("启动 Firefox browser.")
            elif browser == 'Chrome':
                driver = webdriver.Chrome(chrome_driver_path)
                logger.info("启动 Chrome browser.")
            elif browser == "IE":
                driver = webdriver.Ie(ie_driver_path)
                logger.info("启动 IE browser.")
        except  Exception as e:
            logger.error('浏览器启动失败：%s' % repr(e))

        # 打开网址，最大化浏览器，开隐式等待
        driver.get(url)
        logger.info("打开网址: %s" % url)
        driver.maximize_window()
        logger.info("最大化当前窗口.")
        driver.implicitly_wait(5)
        logger.info("设置隐式等待5秒.")
        return driver

    def quit_browser(self):
        logger.info("退出浏览器.")
        self.driver.quit()

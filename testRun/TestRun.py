import unittest
from testRun.HTMLTestRunnerCN import HTMLTestRunner
import os
import time

# 定义输出的文件位置和名字
report_path = os.path.dirname(os.path.abspath('.')) + r'/testReport/'

report_name = report_path + time.strftime("%Y%m%d%H%M%S") + ".html"

# 使用 套件对象，加载对象 去添加用例方法
suite = unittest.TestLoader().discover("testCase")
# 实例化 第三方的运行对象 并运行 套件对象
# HTMLTestRunner()
# stream=sys.stdout ,必填，测试报告的文件对象（open），注意点，要使用wb打开
# verbosity=1，可选，报告的详细程度，默认1 简略，2 详细
# title=None,可选，测试报告的标题
# description=None 可选，描述信息，python的版本，pycharm版本
with open(report_name, "wb") as f:
    runner = HTMLTestRunner(stream=f, title=u"测试报告", description=None, tester=u'PENG CHONG')  # 运行对象
    # 运行对象执行套件
    runner.run(suite)

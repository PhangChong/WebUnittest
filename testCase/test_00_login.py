import os
import unittest
import warnings

from pageObject.test_00 import login
from tool.read_data import get_csv_data


class TestLogin(unittest.TestCase):
    csv_file = os.path.dirname(os.path.abspath('.')) + r"/testData/re_login.csv"

    # csv_file = os.path.abspath(os.path.dirname(os.getcwd())) + r"\testData\re_login.csv"
    @classmethod
    def setUpClass(cls):
        # 每个测试方法执行之前都会调用的方法
        print('------打开浏览器------')

    @classmethod
    def tearDownClass(cls):
        # 每个测试方法执行之都会调用的方法
        # 这句话的作用是用来忽略 ResourceWaring 异常警告的
        warnings.simplefilter("ignore", ResourceWarning)
        print('------退出浏览器------')

    def test_login01(self):
        # test开头
        print("第一条用例测试~")
        data = get_csv_data(self.csv_file, 1)  # 获取csv文件中的第一行数据
        # 预期成功用例（获取第一列和第二列数据）交给 登录
        self.assertEqual('success！', login(data[0], data[1]), )
        # self.assertTrue(login(data[0], data[1]))

    def test_login02(self):  # 获取csv文件中的第二行数据
        print("第二条用例测试~")
        data = get_csv_data(self.csv_file, 2)
        # 预期失败用例
        self.assertEqual('The user does not exist.', login(data[0], data[1]), )

    def test_login03(self):
        print("第三条用例测试~")  # 获取csv文件中的第三行数据
        data = get_csv_data(self.csv_file, 3)
        # 预期失败用例
        self.assertEqual('error！', login(data[0], data[1]), )

    def test_login04(self):
        print("第四条用例测试~")  # 获取csv文件中的第四行数据
        data = get_csv_data(self.csv_file, 4)
        # 预期失败用例
        self.assertEqual('The user does not exist.', login(data[0], data[1]), )


if __name__ == '__main__':
    unittest.main()

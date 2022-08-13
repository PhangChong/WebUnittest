import configparser
import os
from tool.logs import Logs

logger = Logs(logger="ReadConf").getlog()

# 读取配置配件：config.ini
class ReadIni:
    # 初始化 路径
    # 参数1 file_name文件名指定文件名
    # 参数2  node 指定所需要节点名
    def __init__(self, config=None):
        self.config = config
        if config == None:
            config = 'config.ini'
        # os.path.dirname(__file__) 当前路径
        # os.path.dirname(os.path.dirname(__file__)) //（双层）上一层路径
        self.file_name = os.path.dirname(os.path.dirname(__file__)) + "/conf/" + config

        self.cf = self.load_ini(self.file_name)

    # 加载配置文件
    def load_ini(self, file_name):
        # 获取解析配置对象
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        return cf

    # 获取配置文件中的内容===>指定key
    def get(self, node, key):
        try:
            a = self.cf.get(node, key)
            logger.info("读取config:[{}]{}={}".format(node, key, a))
            return a
        except Exception as e:
            # with open('1.txt','a+',encoding='utf8') as f:
            #     f.write(str(e))
            logger.error("读取config属性失败:%s" % e)


if __name__ == '__main__':
    print(ReadIni('conf_debug.ini').get('testSystem', "testing"))
    print(ReadIni('conf_debug.ini').get('testSystem', "test"))

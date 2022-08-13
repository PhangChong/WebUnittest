import logging
import os.path
import time


class Logs(object):
    def __init__(self, logger):
        """
            指定保存日志的文件路径和日志级别，并保持至文件中
        """

        # 创建一个日志器logger
        self.logger = logging.getLogger(logger)

        # 日志输出的默认级别为warning及以上级别，设置输出info级别
        self.logger.setLevel(logging.DEBUG)

        # %Y%m%d%H%M%S
        log_path = os.path.dirname(os.path.abspath('../base')) + r'/logs/'
        log_name = log_path + time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.log'
        # 创建一个文件处理器，文件写入日志
        fh = logging.FileHandler(log_name, encoding="utf8")

        # 创建一个文件处理器,用于控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        # 创建一个文件格式器f_formatter
        f_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(f_formatter)
        sh.setFormatter(f_formatter)

        # 设置处理器输出级别
        fh.setLevel(logging.INFO)

        # 关联控制台日志器—处理器—格式器
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def getlog(self):
        return self.logger


if __name__ == '__main__':

    log = Logs('testLog')
    logger = log.getlog()
    # 输出日志
    try:
        b = int(input("请输入一个除数:"))
        num = 3 / b
        logger.info("3/{}={}".format(b, num))
    except Exception as e:
        logger.error(str(e))

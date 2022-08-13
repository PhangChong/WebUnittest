import time
#读文件
def readFile(url):
    f = open(url, "r")
    s = f.read()
    f.close()
    return s
#写文件
def writeFile(url,String):
    f=open(url,"w")
    f.write(String)
    f.close()
#写日志
def writeLog(String):
    sysTime=time.strftime("[%Y%m%d%H%M%S]")
    f=open(r"..\logs\log.txt","a+")
    f.write(sysTime+String+"\n")
    f.close()
#提取字符串
def reGetString(String,leftBinary,rightBinary):
    import re
    result=re.search("%s(.*?)%s"%(leftBinary,rightBinary),String)
    return result.group(1)

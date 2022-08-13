import re
from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Chrome(r'../adrivers/chromedriver')
dr.get('http://www.baidu.com')
# dr.find_element(By.ID, 'kw').is_displayed()


# def reFindall(rule,matching):
#     a=re.findall(rule, matching)
#     return print(a[0])
#
#
# try:
#     reFindall('alexs','yuanaleSxalexwupeiqi')
#     reFindall('alex','yuanaleSxalexwupeiqi')
# except Exception as e:
#     print(e)

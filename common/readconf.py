import configparser
import os
from common.log import log

#实例化对象
config = configparser.ConfigParser()

#读取ini文件
config.read('..\config\conf.ini',encoding='utf-8')
log('读取到配置文件')
#获取url
url = config.get('LOGIN_URL', 'login_url')
log('获取到登录url为{url}'.format(url=url))
#获取登录账号
username = config.get('LOGIN_INFO', 'username')
log('获取到登录账户为{username}'.format(username=username))

#获取登密码
password = config.get('LOGIN_INFO', 'password')
log('获取到登录密码为{password}'.format(password=password))

#获取api文件目录
apifile_dir = config.get('DIR_PATH', 'apifile')
log('获取到接口文档地址为{apifile_dir}'.format(apifile_dir=apifile_dir))

# 获取测试用例文件目录
testcase_dir = config.get('DIR_PATH', 'testcase')
log('获取到测试用例地址为{testcase_dir}'.format(testcase_dir=testcase_dir))

#获取设备id列表，设备类型参考conf.ini文件说明
devicesidstr= config.get('DEVICESID','devicesidlist')
devicesid=devicesidstr.split(',')

#项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DIR)
#日志目录
LOG_PATH = os.path.join(BASE_DIR,'logs\\')
#报告目录
REPORT_PATH = os.path.join(BASE_DIR,'report\\')


#print(url,username,password,logs_dir,reports_dir,testcase_dir,apifile_dir)




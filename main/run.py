# import sys
# sys.path.append('D:\\APITest')
import unittest
from common.readconf import testcase_dir
from common import HTMLTestRunner
from common.readconf import REPORT_PATH
from common.log import log
import datetime
def addcase():
    log('创建测试集合')
    discovery = unittest.defaultTestLoader.discover(testcase_dir,pattern="test*.py",top_level_dir=None)
    print(discovery)
    suite = unittest.TestSuite()
    suite.addTest(discovery)
    log('集合为{suite}'.format(suite=suite))
    return suite


if __name__ == '__main__':
    now = datetime.datetime.now().strftime('%Y%m%d-%H%M')
    log('开始创建报告')
    f = open(REPORT_PATH + now +'testreport.html', 'wb+')
    log('开始写入报告')
    runner = HTMLTestRunner.HTMLTestRunner(f,title='测试报告',description='接口测试',tester='qizhaojun')
    runner.run(addcase())

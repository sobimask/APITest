from common.log import log
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir


class ChartController(unittest.TestCase):
    '''报表相关接口'''

    def test_ChartController(self):
        log('开始跑测试用例')
        Request().send_request(apifile_dir + 'ChartController.xlsx', 'Sheet1')  ##只需要改动 xxx.xlsx文件即可


if __name__ == '__main__':
    ChartController()

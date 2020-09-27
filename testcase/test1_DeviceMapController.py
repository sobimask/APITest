##测试用例文件，根据模块或者业务逻辑按顺序填写文档地址，
from common.log import log
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir

class DeviceMapController(unittest.TestCase):
    def test_DeviceMapController(self):
        log('开始跑测试用例')
        Request().send_request(apifile_dir+'DeviceMapController.xlsx','Sheet1')   ##只需要改动 xxx.xlsx文件即可

if __name__ == '__main__':
    DeviceMapController()
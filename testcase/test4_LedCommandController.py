from common.log import log
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir
from common.devicesonline import devicesisonline
from common.readconf import devicesid


class Led(unittest.TestCase):
    '''LED屏幕应用操作相关接口'''

    @classmethod
    def setUp(self):
        if devicesisonline(devicesid[1]) == '在线':  # devicesid[1]为LED设备的id
            log("判断设备在线，继续执行")
        else:
            log('设备出于离线状态')
            raise Exception('设备不在线，不执行接口测试')

    def test_EventController(self):
        log('开始跑测试用例')
        Request().send_request(apifile_dir + 'led.xlsx', 'Sheet1')  ##只需要改动 xxx.xlsx文件即可


if __name__ == '__main__':
    Led()

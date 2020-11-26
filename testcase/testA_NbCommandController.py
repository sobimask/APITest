from common.log import log
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir
from common.devicesonline import devicesisonline
from common.readconf import devicesid


class NbCommandController(unittest.TestCase):
    '''NB灯杆操作相关接口'''

    @classmethod
    def setUpClass(cls):
        if devicesisonline(devicesid[4]) == '在线':  # devicesid[4]为灯杆设备的id
            log("判断设备在线，继续执行")
        else:
            log('设备出于离线状态')
            raise Exception('设备不在线，不执行接口测试')

    def test_NbCommandController(self):
        Request().send_request(apifile_dir + 'NbCommandController.xlsx', 'Sheet1')  ##只需要改动 xxx.xlsx文件即可


if __name__ == '__main__':
    NbCommandController()

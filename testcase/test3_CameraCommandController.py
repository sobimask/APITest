from common.log import log
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir
from common.devicesonline import devicesisonline
from common.readconf import devicesid

class Camera(unittest.TestCase):

    '''摄像头应用操作相关接口'''

    def setUp(self) -> None:
        if devicesisonline(devicesid[0]) == '在线':         #devicesid[0]为摄像头设备的id
            log("判断设备在线，继续执行")
        else:
            log('设备出于离线状态')
            raise Exception('设备不在线，不执行接口测试')

    def test_EventController(self):
        log('开始跑测试用例')
        Request().send_request(apifile_dir+'camera.xlsx','Sheet1')   ##只需要改动 xxx.xlsx文件即可

if __name__ == '__main__':
    Camera()

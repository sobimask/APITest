##测试用例文件，根据模块或者业务逻辑按顺序填写文档地址，
from common.log import log
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir
from common.random_data import randomdata
from common.write_excel_data import write_data
class DeviceMapController(unittest.TestCase):
    '''设备地图相关接口'''

    @classmethod
    def setUpClass(cls):
        data = {
            "deviceCriteria": {
                "deviceTypeIds": ["camera"],
                "deviceStatus": ["ONLINE"]
            },
            "criteriaName": randomdata
        }
        write_data(apifile_dir + 'DeviceMapController.xlsx','Sheet1',8,3,str(data))
    def test_DeviceMapController(self):
        log('开始跑测试用例')
        Request().send_request(apifile_dir + 'DeviceMapController.xlsx', 'Sheet1')  ##只需要改动 xxx.xlsx文件即可


if __name__ == '__main__':

    DeviceMapController()

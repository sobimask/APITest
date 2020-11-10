##测试用例文件，根据模块或者业务逻辑按顺序填写文档地址，
from common.log import log
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir
from common.random_data import randomdata
from common.write_excel_data import write_data
class MyTestCase(unittest.TestCase):
    '''
    首页各报表统计
    '''
    def setUp(self) -> None:
        data = {"configurableAttrs": [{"uKey": "serverIp", "value": "11"}, {"uKey": "terid", "value": "11"}],
                "uid": randomdata, "name": randomdata, "deviceModelId": "738682240710184960",
                "appLabelList": {"deviceArea": "003", "manager": "041", "installationDate": "2020-09-07",
                                 "qualityAssuranceDate": "2020-09-23", "installer": "", "supplier": "",
                                 "maintenanceVendor": "", "tags": "", "address": "jianhang)", "production": "",
                                 "deviceType": "", "vehicleId": ""},
                "location": {"coordinateSystemType": "GCJ02", "coordinates": [113.522353, 22.801394], "type": "Point"},
                "deviceType": "Radio",
                "appLabels": [{"key": "deviceArea", "value": "003"}, {"key": "manager", "value": "041"},
                              {"key": "installationDate", "value": "2020-09-07"},
                              {"key": "qualityAssuranceDate", "value": "2020-09-23"},
                              {"key": "address", "value": "jianhang"}]}
        write_data(apifile_dir+'dashboard.xlsx','Sheet',19,3,str(data))

    def test_dashboard(self):
        log('开始跑测试用例')
        Request().send_request(apifile_dir+'dashboard.xlsx','Sheet')   ##只需要改动 xxx.xlsx文件即可

if __name__ == '__main__':
    MyTestCase()

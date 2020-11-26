import json
from common.get_Authorization import Authorization
from common.log import log
import requests
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir
from common.random_data import randomdata
from common.write_excel_data import write_data


class DeviceController(unittest.TestCase):
    '''设备管理相关接口'''

    @classmethod
    def setUpClass(cls):
        adddevice = {"configurableAttrs": [{"uKey": "serverIp", "value": "11"}, {"uKey": "terid", "value": "11"}],
                     "uid": randomdata, "name": randomdata, "deviceModelId": "738682240710184960",
                     "appLabelList": {"deviceArea": "009", "manager": "041", "installationDate": "2020-11-11",
                                      "qualityAssuranceDate": "2022-11-30", "installer": "", "supplier": "",
                                      "maintenanceVendor": "", "tags": "", "address": "广东省广州市南沙区黄阁镇银华街",
                                      "production": "", "deviceType": "", "vehicleId": ""},
                     "location": {"coordinateSystemType": "GCJ02", "coordinates": [113.528413, 22.801362],
                                  "type": "Point"}, "deviceType": "Radio",
                     "appLabels": [{"key": "deviceArea", "value": "009"}, {"key": "manager", "value": "041"},
                                   {"key": "installationDate", "value": "2020-11-11"},
                                   {"key": "qualityAssuranceDate", "value": "2022-11-30"},
                                   {"key": "address", "value": "广东省广州市南沙区黄阁镇银华街"}]}

        headers = {"Authorization": Authorization,
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                 " (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
                   "Content-Type": "application/json;charset=UTF-8"}
        # 新增设备，获取设备id
        adddevice = str(adddevice).encode('utf-8')
        res = requests.post(url='http://island.dev.iot-cas.com:8081/island/device', data=adddevice, headers=headers)
        resjson = json.loads(res.content)
        print(resjson)
        id = resjson['data']['data']
        log('新增设备成功，设备id为{id}'.format(id=id))

        updatedevice = {"configurableAttrs": [{"uKey": "serverIp", "value": "11"}, {"uKey": "terid", "value": 11}],
                        "uid": randomdata + 'up', "name": randomdata + 'up', "deviceModelId": "738682240710184960",
                        "id": id,
                        "appLabelList": {"deviceArea": "009", "manager": "041", "installationDate": "2020-11-11",
                                         "qualityAssuranceDate": "2022-11-30", "installer": "", "supplier": "",
                                         "maintenanceVendor": "", "tags": "", "address": "广东省广州市南沙区黄阁镇银华街",
                                         "production": "", "deviceType": "", "vehicleId": ""},
                        "location": {"coordinateSystemType": "GCJ02", "coordinates": [113.528413, 22.801362],
                                     "type": "Point"}, "realVirtualMark": "REAL", "onlineStatus": "UNACTIVATED",
                        "deviceType": "Radio",
                        "appLabels": [{"key": "deviceArea", "value": "009"}, {"key": "manager", "value": "041"},
                                      {"key": "installationDate", "value": "2020-11-11"},
                                      {"key": "qualityAssuranceDate", "value": "2022-11-30"},
                                      {"key": "address", "value": "广东省广州市南沙区黄阁镇银华街"}]}
        write_data(apifile_dir + 'DeviceController.xlsx', 'Sheet1', 2, 3, str(updatedevice))
        # 写入查询接口id
        getidurl = 'http://island.dev.iot-cas.com:8081/island/devices/getByIds?ids=' + str(id)
        write_data(apifile_dir + 'DeviceController.xlsx', 'Sheet1', 7, 1, str(getidurl))
        # 写入删除接口id
        deletedeviceurl = 'http://island.dev.iot-cas.com:8081/island/devices?ids=' + str(id)
        write_data(apifile_dir + 'DeviceController.xlsx', 'Sheet1', 9, 1, str(deletedeviceurl))

    def test_DeviceController(self):
        log('开始跑测试用例')
        # Request().send_request(apifile_dir + 'DeviceController.xlsx', 'Sheet1')  ##只需要改动 xxx.xlsx文件即可


if __name__ == '__main__':
    DeviceController()

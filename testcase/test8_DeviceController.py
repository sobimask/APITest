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
        adddevice = {
            "configurableAttrs": [],
            "uid": randomdata,
            "name": randomdata,
            "deviceModelId": "786622402234785792",
            "appLabelList": {
                "deviceArea": "001",
                "manager": "001",
                "installationDate": "2020-12-13",
                "qualityAssuranceDate": "2022-12-31",
                "installer": "",
                "supplier": "",
                "maintenanceVendor": "",
                "tags": "",
                "address": "",
                "production": "",
                "deviceType": "",
                "vehicleId": ""
            },
            "location": {
                "coordinateSystemType": "GCJ02",
                "coordinates": [113.525099, 22.79633],
                "type": "Point"
            },
            "deviceType": "WeatherStation",
            "appLabels": [{
                "key": "deviceArea",
                "value": "001"
            }, {
                "key": "manager",
                "value": "001"
            }, {
                "key": "installationDate",
                "value": "2020-12-13"
            }, {
                "key": "qualityAssuranceDate",
                "value": "2022-12-31"
            }]
        }

        headers = {"Authorization": Authorization,
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                 " (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
                   "Content-Type": "application/json;charset=UTF-8"}
        # 新增设备，获取设备id
        adddevice = str(adddevice).encode('utf-8')
        res = requests.post(url='http://island.iot-cas.com:8081/island/device', data=adddevice, headers=headers)
        resjson = json.loads(res.content)
        id = resjson['data']['data']
        log('新增设备成功，设备id为{id}'.format(id=id))

        updatedevice = {
            "configurableAttrs": [],
            "uid": randomdata+"up",
            "name": randomdata+"up",
            "deviceModelId": "786622402234785792",
            "id": id,
            "appLabelList": {
                "deviceArea": "001",
                "manager": "001",
                "installationDate": "2020-12-13",
                "qualityAssuranceDate": "2022-12-31",
                "installer": "",
                "supplier": "",
                "maintenanceVendor": "",
                "tags": "",
                "address": "",
                "production": "",
                "deviceType": "",
                "vehicleId": ""
            },
            "location": {
                "coordinateSystemType": "GCJ02",
                "coordinates": [113.525099, 22.79633],
                "type": "Point"
            },
            "realVirtualMark": "REAL",
            "onlineStatus": "UNACTIVATED",
            "deviceType": "WeatherStation",
            "appLabels": [{
                "key": "deviceArea",
                "value": "001"
            }, {
                "key": "manager",
                "value": "001"
            }, {
                "key": "installationDate",
                "value": "2020-12-13"
            }, {
                "key": "qualityAssuranceDate",
                "value": "2022-12-31"
            }]
        }
        write_data(apifile_dir + 'DeviceController.xlsx', 'Sheet1', 2, 3, str(updatedevice))
        # 写入查询接口id
        getidurl = 'http://island.iot-cas.com:8081/island/devices/getByIds?ids=' + str(id)
        write_data(apifile_dir + 'DeviceController.xlsx', 'Sheet1', 7, 1, str(getidurl))
        # 写入删除接口id
        deletedeviceurl = 'http://island.iot-cas.com:8081/island/devices?ids=' + str(id)
        write_data(apifile_dir + 'DeviceController.xlsx', 'Sheet1', 9, 1, str(deletedeviceurl))

    def test_DeviceController(self):
        log('开始跑测试用例')
        # Request().send_request(apifile_dir + 'DeviceController.xlsx', 'Sheet1')  ##只需要改动 xxx.xlsx文件即可


if __name__ == '__main__':
    DeviceController()

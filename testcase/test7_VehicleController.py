import json
from common.get_Authorization import Authorization
from common.log import log
import requests
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir
from common.random_data import randomdata
from common.write_excel_data import write_data
class VehicleController(unittest.TestCase):
    '''载体相关接口'''

    def setUp(self):
        data1 = {
            "uid": randomdata,
            "type": "LIGHTPOLE",
            "name": randomdata,
            "deviceArea": "001",
            "manager": "001",
            "installationDate": "2020-11-10",
            "qualityAssuranceDate": "2020-11-30",
            "address": "广东省广州市南沙区黄阁镇广州南沙政务服务中心广州市南沙区人民政府",
            "status": "NORMAL",
            "location": {
                "coordinateSystemType": "GCJ02",
                "coordinates": [113.526816, 22.801711],
                "type": "Point"
            }
        }
        write_data(apifile_dir + 'VehicleController.xlsx','Sheet1',2,3,str(data1))

        headers = {"Authorization": Authorization,
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                 " (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
                   "Content-Type": "application/json;charset=UTF-8"}
        #新增载体，获取载体id
        #data1=data1.encode('utf-8')
        res = requests.post('http://island.dev.iot-cas.com:8081/island/vehicle', data=data1, headers=headers)
        resjson = json.loads(res.content)
        print(resjson)
        id=resjson['data']
        print(id)
        updatedata = {
            "uid": "111",
            "type": "LIGHTPOLE",
            "name": "11",
            "deviceArea": "001",
            "manager": "001",
            "installationDate": "2020-11-10",
            "qualityAssuranceDate": "2020-11-29",
            "address": "广东省广州市南沙区南沙街道南沙碧桂园倚荔轩南沙碧桂园-漾月轩",
            "status": "NORMAL",
            "location": {
                "coordinateSystemType": "GCJ02",
                "coordinates": [113.555655, 22.794303],
                "type": "Point"
            },
            "id": id
        }
        write_data(apifile_dir + 'VehicleController.xlsx', 'Sheet1', 3, 3, str(updatedata))

    def test_VehicleController(self):
        log('开始跑测试用例')
        Request().send_request(apifile_dir + 'VehicleController.xlsx', 'Sheet1')  ##只需要改动 xxx.xlsx文件即可


if __name__ == '__main__':

    VehicleController()
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

    @classmethod
    def setUpClass(cls):
        data1 = {
            "uid": randomdata,
            "type": "LIGHTPOLE",
            "name": randomdata,
            "deviceArea": "001",
            "manager": "001",
            "installationDate": "2020-12-14",
            "qualityAssuranceDate": "2022-12-29",
            "address": "广东省广州市南沙区南沙街道逸涛雅苑",
            "status": "NORMAL",
            "location": {
                "coordinateSystemType": "GCJ02",
                "coordinates": [113.536772, 22.80361],
                "type": "Point"
            }
}

        headers = {"Authorization": Authorization,
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                 " (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
                   "Content-Type": "application/json;charset=UTF-8"}
        # 新增载体，获取载体id
        data1 = str(data1).encode('utf-8')
        res = requests.post(url='http://island.iot-cas.com:8081/island/vehicle', data=data1, headers=headers)
        resjson = json.loads(res.content)
        id = resjson['data']
        log('新增载体成功，载体id为{id}'.format(id=id))

        updatedata = {
            "uid": randomdata + "up",
            "type": "LIGHTPOLE",
            "name": randomdata + "up",
            "deviceArea": "001",
            "manager": "001",
            "installationDate": "2020-12-14",
            "qualityAssuranceDate": "2022-12-29T00:00:00",
            "address": "广东省广州市南沙区南沙街道逸涛雅苑",
            "status": "NORMAL",
            "location": {
                "coordinateSystemType": "GCJ02",
                "coordinates": [113.536772, 22.80361],
                "type": "Point"
            },
            "id": id
        }

        updateurl = 'http://island.iot-cas.com:8081/island/vehicles?ids=' + id
        write_data(apifile_dir + 'VehicleController.xlsx', 'Sheet1', 2, 3, str(updatedata))
        write_data(apifile_dir + 'VehicleController.xlsx', 'Sheet1', 7, 1, str(updateurl))

    def test_VehicleController(self):
        log('开始跑测试用例')
        Request().send_request(apifile_dir + 'VehicleController.xlsx', 'Sheet1')  ##只需要改动 xxx.xlsx文件即可


if __name__ == '__main__':
    VehicleController()

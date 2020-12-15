##测试用例文件，根据模块或者业务逻辑按顺序填写文档地址，
import json
import requests
from common.get_Authorization import Authorization
from common.log import log
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir
from common.random_data import randomdata
from common.write_excel_data import write_data


class IlluminationCommandController(unittest.TestCase):
    '''
    策略相关接口
    '''

    @classmethod
    def setUpClass(cls):
        data1 = {
            "templateName": randomdata,
            "description": "",
            "priority": 0,
            "executeDateMode": "DAILY",
            "operation": "LIGHT_ON",
            "startEndPeriodDimming": [{
                "dimmingStartTime": "18:30:00",
                "dimmingEndTime": "07:30:00",
                "dimmingValue": 100
            }],
            "validStartDate": "2020-11-01",
            "validEndDate": ""
        }
        headers = {"Authorization": Authorization,
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                 " (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
                   "Content-Type": "application/json;charset=UTF-8"}

        # 新增策略模板，获取载模板id
        data1 = str(data1).encode('utf-8')
        res = requests.post(url='http://island.iot-cas.com:8081/island/illumination/template', data=data1,
                            headers=headers)
        resjson = json.loads(res.content)
        id = resjson['data']

        # 不绑定策略实例，供删除策略模板接口使用
        res2 = requests.post(url='http://island.iot-cas.com:8081/island/illumination/template', data=data1,
                             headers=headers)
        resjson2 = json.loads(res2.content)
        delid = resjson2['data']

        # 写入删除智能照明策略模板url
        delurl = 'http://island.iot-cas.com:8081/island/illumination/template?ids=' + delid
        write_data(apifile_dir + 'IlluminationCommandController.xlsx', 'Sheet1', 11, 1, str(delurl))

        # 写入查询策略接口url
        url = 'http://island.iot-cas.com:8081/island/illumination/template/' + id
        write_data(apifile_dir + 'IlluminationCommandController.xlsx', 'Sheet1', 2, 1, str(url))
        # 写入查询智能照明策略模板是否允许被编辑接口url
        url1 = 'http://island.iot-cas.com:8081/island/illumination/isEditable/' + id
        write_data(apifile_dir + 'IlluminationCommandController.xlsx', 'Sheet1', 3, 1, str(url1))

        # 新建策略实例
        data2 = {
            "templateId": id,
            "deviceIdList": ["773475252786049024"]
        }
        data2 = str(data2).encode('utf-8')
        res1 = requests.post(url='http://island.iot-cas.com:8081/island/illumination/releaseStrategy', data=data2,
                             headers=headers)
        resjson1 = json.loads(res1.content)
        id1 = resjson1['data']

        # 写入开启/关闭策略实例url
        url3 = 'http://island.iot-cas.com:8081/island/illumination/switchOnOffStrategy?id=' + id1 + '&isTurnOn=true'
        write_data(apifile_dir + 'IlluminationCommandController.xlsx', 'Sheet1', 9, 1, str(url3))

        # 写入查询策略实例接口url
        url2 = 'http://island.iot-cas.com:8081/island/illumination/queryStrategyDetail?id=' + id1
        write_data(apifile_dir + 'IlluminationCommandController.xlsx', 'Sheet1', 8, 1, str(url2))

        # 写入修改策略数据
        updata = {
            "templateName": randomdata,
            "description": "",
            "priority": 0,
            "executeDateMode": "DAILY",
            "operation": "LIGHT_ON",
            "startEndPeriodDimming": [{
                "dimmingStartTime": "18:30:00",
                "dimmingEndTime": "07:30:00",
                "dimmingValue": 105
            }],
            "validStartDate": "2020-11-01",
            "validEndDate": "",
            "id": id
        }
        write_data(apifile_dir + 'IlluminationCommandController.xlsx', 'Sheet1', 7, 3, str(updata))

        # 写入删除实例接口url
        delurl1 = 'http://island.iot-cas.com:8081/island/illumination/deleteStrategy?id=' + id1
        write_data(apifile_dir + 'IlluminationCommandController.xlsx', 'Sheet1', 12, 1, str(delurl1))

    def test_IlluminationCommandController(self):
        log('开始跑测试用例')
        Request().send_request(apifile_dir + 'IlluminationCommandController.xlsx', 'Sheet1')  ##只需要改动 xxx.xlsx文件即可


if __name__ == '__main__':
    IlluminationCommandController()

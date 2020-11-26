import requests
import json
from common.get_Authorization import Authorization


def devicesisonline(devices):
    '''获取各类测试设备在线情况'''
    headers = {"Authorization": Authorization,
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                             " (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
               "Content-Type": "application/json;charset=UTF-8"}

    url = 'http://island.dev.iot-cas.com:8081/island/device/query/device'
    res = requests.get(url=url, params=devices, headers=headers)
    resjson = json.loads(res.content)
    status = resjson['data']['onlineStatusName']
    return status

# print(devicesisonline())


# class Devices_Online():

# def cameraisonline(self):
#     # 获取测试摄像头在线情况
#     # 测试室摄像头id=720586611470512128
#     url = 'http://island.dev.iot-cas.com:8081/island/device/query/device'
#     res = requests.get(url=url,params ='id=720586611470512128',headers = Devices_Online().headers)
#     resjson = json.loads(res.content)
#     status = resjson['data']['onlineStatusName']
#     return status
#
# def ledisonline(self):
#     #获取测试LED屏在线情况
#     #测试LED屏id=741344626406817792
#     url = 'http://island.dev.iot-cas.com:8081/island/device/query/device'
#     res = requests.get(url=url, params='id=741344626406817792', headers=Devices_Online().headers)
#     resjson = json.loads(res.content)
#     status = resjson['data']['onlineStatusName']
#     return status
#
# def broadcastisonline(self):
#     # 获取测试广播在线情况
#     # 测试广播id=719573907100286976
#     url = 'http://island.dev.iot-cas.com:8081/island/device/query/device'
#     res = requests.get(url=url, params='id=719573907100286976', headers=Devices_Online().headers)
#     resjson = json.loads(res.content)
#     status = resjson['data']['onlineStatusName']
#     return status
#
# def talkieisonline(self):
#     # 获取测试对讲设备在线情况
#     # 测试对讲设备id=703191838758821888
#     url = 'http://island.dev.iot-cas.com:8081/island/device/query/device'
#     res = requests.get(url=url, params='id=703191838758821888', headers=Devices_Online().headers)
#     resjson = json.loads(res.content)
#     status = resjson['data']['onlineStatusName']
#     return status


# print(Devices_Online().devicesisonline(Devices_Online().broadcasid))


import requests
import json
from common.get_Authorization import Authorization


def devicesisonline(devices):
    '''获取各类测试设备在线情况'''
    headers = {"Authorization": Authorization,
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                             " (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
               "Content-Type": "application/json;charset=UTF-8"}

    url = 'http://island.iot-cas.com:8081/island/device/query/device'
    res = requests.get(url=url, params=devices, headers=headers)
    resjson = json.loads(res.content)
    status = resjson['data']['onlineStatusName']
    return status
# print(Devices_Online().devicesisonline(Devices_Online().broadcasid))

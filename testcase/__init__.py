import json

import requests
from common.get_Authorization import Authorization
from requests_toolbelt import MultipartEncoder

m = MultipartEncoder(
    fields={'alarmEventIdList': '776864709486383104', 'applyContent': 'apitest',
            'endDateTime': '2022-11-30 00:00:00',
            'files': ('1.txt', open(file='../media/1.txt', mode='rb'), 'text/plain'),
            'handleDepartmentId': '037', 'handleDepartmentName': '测试部门',
            'handleUserId': '719967562599632896', 'handleUserName': 'admin1', 'handleUserTel': '13333333332',
            'originTypeCode': '0', 'priorityLevelCode': '0', 'startDateTime': '2020-11-20 15:48:14',
            })
print(m.content_type)

res = requests.request(method='post', url='http://island.dev.iot-cas.com:8081/island/ticketSys/tickets', data=m,
                       headers={"Authorization": Authorization,
                                'Content-Length': '1276',
                                'Access-Control-Allow-Origin': '*',
                                'Accept': 'application/json, text/plain, */*',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                                'Content-Type': m.content_type,
                                'Accept-Encoding': 'gzip, deflate',
                                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
                                })
resjson = json.loads(res.content)
print(resjson)
id = resjson['data']['id']
fileid = resjson['data']['fileIdList'][0]
url1 = 'http://island.dev.iot-cas.com:8081/island/ticketSys/tickets/' + id + '/files/' + fileid + ''
print(res.text)
print(id)
print(fileid)
print(url1)

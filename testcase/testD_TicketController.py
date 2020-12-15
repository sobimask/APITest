import json
import requests
from common.get_Authorization import Authorization
from common.log import log
import unittest
from common.requests_http import Request
from common.readconf import apifile_dir
from common.random_data import randomdata
from common.write_excel_data import write_data
from requests_toolbelt import MultipartEncoder


class TicketController(unittest.TestCase):
    '''
    工单相关接口
    '''

    @classmethod
    def setUpClass(cls):
        # 新增工单
        data = MultipartEncoder(
            fields={'alarmEventIdList': '776864709486383104', 'applyContent': 'apitest',
                    'endDateTime': '2022-11-30 00:00:00',
                    'files': ('1.txt', open(file='../media/1.txt', mode='rb'), 'text/plain'),
                    'handleDepartmentId': '037', 'handleDepartmentName': '测试部门',
                    'handleUserId': '719967562599632896', 'handleUserName': 'admin1', 'handleUserTel': '13333333332',
                    'originTypeCode': '0', 'priorityLevelCode': '0', 'startDateTime': '2020-11-20 15:48:14',
                    })
        res = requests.request(method='post', url='http://island.iot-cas.com:8081/island/ticketSys/tickets',
                               data=data,
                               headers={"Authorization": Authorization,
                                        'Content-Length': '1276',
                                        'Access-Control-Allow-Origin': '*',
                                        'Accept': 'application/json, text/plain, */*',
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                                        'Content-Type': data.content_type,
                                        'Accept-Encoding': 'gzip, deflate',
                                        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'})
        log('新增工单完成')
        # 获取新增工单id和文件id
        resjson = json.loads(res.content)
        id = resjson['data']['id']  # 工单id
        fileid = resjson['data']['fileIdList'][0]  # 工单附件id
        url = 'http://island.iot-cas.com:8081/island/ticketSys/tickets/' + id  # 工单url
        write_data(apifile_dir + 'TicketController.xlsx', 'Sheet1', 4, 1, str(url))  # 写入查询工单详情url
        write_data(apifile_dir + 'TicketController.xlsx', 'Sheet1', 6, 1, str(url))  # 写入删除工单url
        url1 = 'http://island.iot-cas.com:8081/island/ticketSys/tickets/' + id + '/files/' + fileid + ''  # 工单附件url
        write_data(apifile_dir + 'TicketController.xlsx', 'Sheet1', 5, 1, str(url1))  # 写入删除工单附件url
        log('写入工单各url完成')

        data1 = MultipartEncoder(
            fields={'ticketId': id, 'workflowStatusCode': '1001', 'operateRemark': 'test'})
        res1 = requests.request(method='post', url='http://island.iot-cas.com:8081/island/ticketSys/tickets/' + id,
                                data=data1,
                                headers={"Authorization": Authorization,
                                         'Content-Length': '1276',
                                         'Access-Control-Allow-Origin': '*',
                                         'Accept': 'application/json, text/plain, */*',
                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                                         'Content-Type': data.content_type,
                                         'Accept-Encoding': 'gzip, deflate',
                                         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
                                         })

        log('更新工单接口完成')

    def test_TicketController(self):
        Request().send_request(apifile_dir + 'TicketController.xlsx', 'Sheet1')


if __name__ == '__main__':
    TicketController()

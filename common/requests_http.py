#coding=utf-8
#封装各种请求接口，
import unittest
import requests
import json
from common.get_Authorization import Authorization
from common.readcase import ReadCase
from common.readconf import apifile_dir
from common.log import log
import json
import datetime

class Request(unittest.TestCase):

        log(u'准备发送请求')
        def send_request(self,api_file=None,case_sheet=None):
            #定义请求头，把Authorization放在这里
            global res
            headers = {"Authorization":Authorization,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                        " (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44","Content-Type":"application/json;charset=UTF-8"}
            log('请求头为{headers}'.format(headers=headers))
            #读取接口文档的信息，url，method等
            log('开始循环获取api文档每一行的数据存为列表')
            for list in ReadCase().get_rows_data(api_file,case_sheet):
                url = list[0]
                mothod = list[1]
                data = list[2]
                code = list[3]
                status= list[4]
                params = list[5]
                apiname = list[6]
                log('此次请求信息列表{list}'.format(list=list))
                #判断mothod是什么类型，从而采用什么请求方式
                log('开始判断请求方式')
                if mothod == 'get':
                    res = requests.get(url, headers= headers,params=params)
                    log('判断为get,并完成请求')
                elif mothod == 'post':
                    if data != None:
                        data = data.encode('utf-8')
                        res = requests.post(url,data=data,headers = headers,params = params)
                        log('判断为post,并完成请求')
                elif  mothod == 'put':
                    res = requests.put(url,data=data,headers = headers)
                    log('判断为put,并完成请求')
                elif mothod == 'delete':
                    res = requests.delete(url,data=data,headers = headers)
                    log('判断为delete,并完成请求')
                rescode = res.status_code
                restext = res.text
                #print(res.text)
                #判断请求是否成功，成功后再根据返回值判断返回具体信息，不成功直接抛出错误
                if 200 == rescode:
                    log('请求响应预期200，实际为{rescode}'.format(rescode=rescode))
                    resjson = json.loads(res.content)
                    resjson_code = resjson['code']
                    resjson_status = resjson['status']
                    resjson_msg = resjson['msg']
                    log('返回结果为{restext}'.format(restext=restext))

                    print(url,apiname,'请求完成,返回code和status和msg提示分别是',resjson_code,resjson_status,resjson_msg)
                    self.assertEqual(resjson_code, code) and self.assertEqual(status, resjson_status)
                    log('判断预期和实际返回信息完成')
                else:
                    log('请求不为200')
                    raise Exception('接口通信失败，请检查网络')

if __name__ == '__main__':
    #Request().send_request(apifile_dir + 'dashboard.xlsx', 'Sheet')
    unittest.mian()
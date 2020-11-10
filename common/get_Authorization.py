##本系统接口不采用token或者cookie来验证登录，采用Authorization秘钥验证登录
##对于接口自动化来说，无论cookie还是Authorization，只要获取到值后，放在请求头中，就可以保持登录
##此文件是请求登录接口，获取到登录成功后返回的Authorization

import requests
import json
from common.readconf import url, username, password
from common.log import log
class GetLogin:
     #获取登录态秘钥
    log('开始登陆')
    def login(self):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple'
                                'WebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
        data = {'username': username,
                'password': password}
        res = requests.post(url, headers=header, data=data).content
        log('登录完成获取信息')
#        print(res)
        resjson = json.loads(res)
        # 尝试获取登录返回信息，登录错误提示
        try:
            msg = resjson['msg']
            if msg == '用户名或密码错误':
                print(msg)
                log(msg)
        except:
            # 登录成功获取Authorization
            AuthorizationType = resjson['data']['tokenType']
            AuthorizationValue = resjson['data']['value']
            cookie = GetLogin.cookie = AuthorizationType + ' ' + AuthorizationValue #str类型
            #cookie1 = {'Authorization': cookie} #元组类型
            #print(cookie)
            return cookie
            log('返回登录秘钥为{cookie}'.format(cookie=cookie))
Authorization = GetLogin().login()  # 赋值变量供传递 元组类型

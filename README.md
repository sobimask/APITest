# APITest 灯杆云接口自动化

框架说明

  1.apifile  --存在用例excel文件
  
  2.common   --一些公用方法，封装函数
    
    devicesisonline.py --获取设备在线状态
    get_Authorization.py --获取登录态，供用例运行时鉴权
    HTMLTestRunner.py --测试报告HTML样式模板
    log.py --封装日志功能
    random_data.py --封装随机值函数
    readcase.py --封装读取excel文件方法函数
    readconf.py --封装读取配置文件方法函数
    reqeuests_http.py --封装接口请求方法函数
    wirte_excel_data.py --封装写入excel文件方法函数
    
  3.config   --框架基础配置，如用户信息，文件路径
  
  4.logs     --运行日志存放目录
  
  5.main     --框架运行入口，扫描所有用例，全部执行
  
  6.report   --测试报告目录
 
  7.testcase --模块用例
  
    test1_DeviceMapController.py --设备地图相关接口
    test2_EventController.py --事件相关接口
    test3_CameraCommandController.py  --摄像头操作相关接口
    test4_LedCommandController.py  --led屏幕操作相关接口
    test5_RadioCommandController.py  --广播操作相关接口
    test6_dashboard.py --获取报表数据相关接口
    
  
  
  

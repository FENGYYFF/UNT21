# 首先要理解我们要调用的模块是TextTestRunner，但是这是文本的，所以我们用具有UI界面的模块
import HTMLTestRunnerNew
# 导入刚刚完成装填的suite
from testdata.testsuite_register_v5 import suite_register

# 创建一个文件类对象，读写模式开启
with open('html_result/test_report.html','wb+') as file:
    # 开始调用runner()这个方法，填入适当的配置参数，创建出一个runner对象
    runner = HTMLTestRunnerNew.HTMLTestRunner(file,
                                            title='Register接口测试报告',
                                            description='测试报告作业====自我练习',
                                            tester='小冯本冯')
    # 让这个对象调用run这个方法从而开始用例执行输出，入参为suite
    runner.run(suite_register)


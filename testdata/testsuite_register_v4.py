import unittest
from testcase.testcase_register_v2 import TestRegister_V2
from common.read_excel_v2 import ReadExcel

# 创建一个suite对象
suite_register = unittest.TestSuite()

# 调用class 读取函数
readxl = ReadExcel("../testdata/data_xl.xlsx", "login_sheet")

testdata = readxl.getTestData()

for i in testdata:
    suite_register.addTest(TestRegister_V2("testLogin",eval(i.data), eval(i.expect)))
# for i in testdata:
#     suite_register.addTest(test_register(eval(i["data"]), eval(i["expect"])))


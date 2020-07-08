import unittest
from testdata.testcase_register import test_register
from common.read_excel import ReadExcel

# 创建一个suite对象
suite_register = unittest.TestSuite()

# 调用class 读取函数
readxl = ReadExcel("../testdata/data_xl.xlsx","login_sheet")
testdata = readxl.getTestData()


for i in testdata:
    suite_register.addTest(test_register(eval(i["data"]),eval(i["expect"])))
import unittest
from common.loginfuc import register
from ddt import ddt,data
from common.read_excel_v2 import ReadExcel




@ddt
class TestRegister_V2(unittest.TestCase):
    testdata = ReadExcel("../testdata/data_xl.xlsx", "login_sheet").getTestData()
    # testcase01： 成功注册
    @data(*testdata)
    def testLogin(self,testdata):
        # 预制数据
        data = eval(testdata.data)
        # 期待结果
        expect = eval(testdata.expect)
        # 创建register对象，返回接口response
        response = register(*data)
        try:
            # 对返回值进行断言判断
            self.assertEqual(response, expect)
            print('返回值是：',response)
        except AssertionError as e:
            print('用例失败， 失败原因： {}'.format(e))
            raise e


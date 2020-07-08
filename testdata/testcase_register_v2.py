import unittest
from common.loginfuc import register

class TestRegister_V2(unittest.TestCase):
    def __init__(self,method,data,expect):
        super().__init__(method)
        self.data = data
        self.expect = expect
    # testcase01： 成功注册
    def testLogin(self):
        # 预制数据
        data = self.data
        # 期待结果
        expect = self.expect
        # 创建register对象，返回接口response
        response = register(*data)
        try:
            # 对返回值进行断言判断
            self.assertEqual(response, expect)
            print('返回值是：',response)
        except AssertionError as e:
            print('用例失败， 失败原因： {}'.format(e))
            raise e


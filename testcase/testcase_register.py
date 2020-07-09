"""
import unittest
from common.loginfuc import register

class test_register(unittest.TestCase):
    def __init__(self,data,expect):
        super().__init__('test_login')
        self.data = data
        self.expect = expect
    # testcase01： 成功注册
    def test_login(self):
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





    # # testcase02： 用户已存在
    # def test_customer_existed(self):
    #     # 创建register对象，返回接口response
    #     response = register('python18', 123456, 123456)
    #     # 对返回值进行断言判断
    #     self.assertEqual(response, {'code': 0, 'msg': '用户已存在'})
    #
    # # testcase03： 两次密码不一致
    # def test_password_not_same(self):
    #     response = register('python199', 123456, 123465456)
    #     self.assertEqual(response,{'code': 0, 'msg': '输入的两次密码不一致'})
    #
    # # testcase04: 长度太短
    # def test_length_incorrect(self):
    #     response = register('py8', 1256, 1256)
    #     self.assertEqual(response, {'code': 0, 'msg': '账号和密码的长度需要在6-18位之间'})

"""
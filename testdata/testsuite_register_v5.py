import unittest


# 创建一个suite对象
suite_register = unittest.TestSuite()
loader = unittest.TestLoader()
suite_register.addTest(loader.discover(r'/Users/feng./PycharmProjects/automation21/testcase'))

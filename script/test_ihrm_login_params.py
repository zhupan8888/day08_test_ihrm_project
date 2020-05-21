import unittest
import logging
import requests

import app
from utils import assert_common, read_login_data
from parameterized import parameterized


# 创建测试类，继承unittest.TestCase
class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        from api.login_api import TestLoginApi  # 导入封装的API模块
        self.login_api = TestLoginApi()  # 实例化登录API

    # 定义数据文件的路径
    filename = app.BASE_DIR + "/data/login_data.json"

    @parameterized.expand(read_login_data(filename))
    # 编写第一个案例，测试登录成功
    def test01_login_success(abc, case_name, jsonData, http_code, success, code, message):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = jsonData
        # 发送登录请求
        response = abc.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # # 断言登录的结果
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, result.get("success"))  # 断言success
        # self.assertEqual(10000, result.get("code"))  # 断言code
        # self.assertIn("操作成功", result.get("message"))  # 断言message

        # 使用封装的通用断言函数实现优化断言
        assert_common(http_code, success, code, message, response, abc)

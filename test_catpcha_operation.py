# -*- coding: utf-8 -*-
"""
 @Author: xiaoxuan6
 @Date: 2025/8/3 14:53
 @File: test_catpcha_operation.py
 @Description: 
"""
import os.path
import unittest

from captcha_operation.operation import operation


class OperationTest(unittest.TestCase):
    def test_operation(self):
        filepath = os.path.join(os.path.dirname(__file__), 'captcha.png')
        self.assertEqual(10, operation(filepath), 'ok')


if __name__ == '__main__':
    unittest.main()

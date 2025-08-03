# -*- coding: utf-8 -*-
"""
 @Author: xiaoxuan6
 @Date: 2025/8/3 14:53
 @File: test_catpcha_operation.py
 @Description: 
"""
import os.path
import unittest

from PIL import Image

from captcha_operation.operation import operation


class OperationTest(unittest.TestCase):
    def test_operation(self):
        # bytes
        filepath = os.path.join(os.path.dirname(__file__), 'captcha.png')
        self.assertEqual(10, operation(open(filepath, 'rb').read()), 'ok')

        # Image
        self.assertEqual(10, operation(Image.open(filepath)), 'ok')

        # str (base64 需要將前缀去掉：data:image/png;base64,)
        self.assertEqual(1, operation(
            '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'),
                         'ok')


if __name__ == '__main__':
    unittest.main()

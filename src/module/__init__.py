#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
    @Author:V7hinc
    @Datetime:2020/11/25 10:31
    @Software:PyCharm
    @Filename:__init__.py
"""

# 正式代码
import os
import sys
current_py_path = os.path.dirname(os.path.abspath(__file__))
if current_py_path not in sys.path:
    sys.path.insert(1, current_py_path)

#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
    @Author:V7hinc
    @Datetime:2021/1/28 15:17
    @Software:PyCharm
    @Filename:setting.py
"""

# 正式代码
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.isdir(LOG_DIR):
    os.makedirs(LOG_DIR)


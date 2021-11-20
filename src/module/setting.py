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
import platform
import stat
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.isdir(LOG_DIR):
    os.makedirs(LOG_DIR)

# 识别当前操作系统
os_plat = platform.system()
if os_plat == 'Windows':
    print('Windows系统')
    chrome_driver_name = 'chromedriver_win32.exe'
elif os_plat == 'Linux':
    print('Linux系统')
    chrome_driver_name = 'chromedriver_linux64'
elif os_plat == 'Darwin':
    print('Darwin系统')
    chrome_driver_name = 'chromedriver_mac64'
else:
    print('其他')
    chrome_driver_name = 'chromedriver_linux64'

chrome_driver = os.path.join(os.path.dirname(BASE_DIR), 'rely', chrome_driver_name)
os.chmod(chrome_driver, stat.S_IRWXU+stat.S_IRWXG)  # 如果没有执行权限，首次需要执行该命令

if os_plat == 'Windows':
    browsermob_proxy = os.path.join(os.path.dirname(BASE_DIR), "rely", "browsermob-proxy-2.1.4/bin/browsermob-proxy.bat")
else:
    browsermob_proxy = os.path.join(os.path.dirname(BASE_DIR), "rely", "browsermob-proxy-2.1.4/bin/browsermob-proxy")
    os.chmod(browsermob_proxy, stat.S_IRWXU + stat.S_IRWXG)  # 如果没有执行权限，首次需要执行该命令

ffmpeg = "ffmpeg"
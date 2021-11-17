#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
    @Author:V7hinc
    @Datetime:2021/11/15 10:52
    @Software:PyCharm
    @Filename:1.py
"""

# 正式代码
# pip install browsermob-proxy
# https://github.com/lightbody/browsermob-proxy/releases
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import platform
import stat
from module.setting import BASE_DIR
from module.get_html_title import get_html_title
from module.m3u8Downloader import m3u8Downloader


def get_args():
    import argparse

    parser = argparse.ArgumentParser()
    # 设置参数组required
    req_grp = parser.add_argument_group('required')
    req_grp.add_argument('-u', action="store", required=True, dest='video_url', nargs=1, type=str, help='''使用https://www.kan.cc的视频链接，并使用第一集的链接，其他不保证能用，例如：https://www.kan.cc/play/2563-0-0.html''')
    # 默认是可选组
    args = parser.parse_args()
    return args


# 是被当前操作系统
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

chrome_driver = os.path.join(BASE_DIR, 'rely', chrome_driver_name)
os.chmod(chrome_driver, stat.S_IRWXU+stat.S_IRWXG)  # 如果没有执行权限，首次需要执行该命令


def get_m3u8_link(video_url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 开启无界面模式
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')  # 关闭浏览器沙箱
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)  # 不加载图片
    chrome_options.add_argument('--ignore-certificate-errors')  # 自动接受网站的不安全证书
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    # 要访问的地址
    proxy.new_har("ht_list2", options={'captureContent': True})

    driver.get(video_url)
    # 此处最好暂停几秒等待页面加载完成，不然会拿不到结果
    driver.implicitly_wait(1)
    time.sleep(1)
    result = proxy.har

    result_url = None
    for entry in result['log']['entries']:
        _url = entry['request']['url']
        # # 根据URL找到数据接口
        if _url.endswith(".m3u8"):
            result_url = _url
            break
    driver.quit()
    return result_url


if __name__ == '__main__':
    args = get_args()
    video_url = args.video_url[0]
    if os_plat == 'Windows':
        server = Server(os.path.join(BASE_DIR, "rely", "browsermob-proxy-2.1.4/bin/browsermob-proxy.bat"))
    else:
        proxy_path = os.path.join(BASE_DIR, "rely", "browsermob-proxy-2.1.4/bin/browsermob-proxy")
        os.chmod(proxy_path, stat.S_IRWXU + stat.S_IRWXG)  # 如果没有执行权限，首次需要执行该命令
        server = Server(proxy_path)

    server.start()  # 启动代理服务器
    proxy = server.create_proxy()

    # 开始扫描视频
    m3u8_url_list = []
    videoNameList = []
    video_dir = os.path.join(BASE_DIR, 'log', "未识别到路径")

    base_url = video_url  # 第一集的url
    next_episode = base_url
    while next_episode is not None:
        html_info = get_html_title(next_episode)
        m3u8_link = get_m3u8_link(next_episode)
        m3u8_url_list.append(m3u8_link)
        title = html_info.get('title', '无名')
        videoNameList.append(title)
        print(f'标题：{title}, 视频链接：{next_episode}, m3u8链接：{m3u8_link}')
        video_dir = title.split(' ', 1)[0]
        next_episode = html_info.get('next_episode')
    print(f'{video_dir} 共 {len(m3u8_url_list)} 集')
    if len(m3u8_url_list) > 0:
        m3u8Downloader(m3u8_url_list, videoNameList, os.path.join(BASE_DIR, 'log', video_dir))

    server.stop()


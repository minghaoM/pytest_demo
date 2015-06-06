# -*- coding: utf-8 -*-
"""
description: 模拟浏览器的基类
"""
__author__ = "sa"


class BrowserBase(object):

    def launch(self):
        # 模拟打开浏览器
        print("launch browser")

    def exit(self):
        # 模拟退出浏览器
        print("exit browser")

    def open_url(self, url):
        # 模拟打开url
        print("open url: {0}".format(url))

    def go_back(self):
        # 模拟回退动作
        print("go back")


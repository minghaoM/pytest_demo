# -*- coding: utf-8 -*-
"""
description: 模拟浏览器的基类
"""
__author__ = "cm"


class BrowserBase(object):

    def launch(self):
        # 模拟打开浏览器
        print("##Mock: launch browser")

    def exit(self):
        # 模拟退出浏览器
        print("##Mock: exit browser")

    def open_url(self, url):
        # 模拟打开url
        print("##Mock: open url: {0}".format(url))

    def go_back(self):
        # 模拟回退动作
        print("##Mock: go back")


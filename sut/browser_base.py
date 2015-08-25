# -*- coding: utf-8 -*-
"""
description: 模拟浏览器的基类
"""
__author__ = "cm"


class BrowserBase(object):

    def launch(self):
        """
        模拟打开浏览器
        """
        print("##Mock: launch browser")

    def exit(self):
        """
        模拟退出浏览器
        """
        print("##Mock: exit browser")
        return True

    def open_url(self, url):
        """
        模拟打开url
        """
        print("##Mock: open url: {0}".format(url))
        return True

    def open_tab(self):
        """
        模拟打开新标签
        """
        print("##Mock: open tab: {0}")
        return True

    def switch_tab(self, tab_index=-1):
        """
        模拟切换标签
        """
        print("##Mock: switch tab: {0}".format(tab_index))
        return True

    def get_current_url(self, mock_url):
        """
        模拟获取当前url
        """
        print("##Mock: get current url: {0}".format(mock_url))
        return mock_url

    def go_back(self):
        """
        模拟回退动作
        """
        print("##Mock: go back")
        return True

    def go_forward(self):
        """
        模拟前进动作
        """
        print("##Mock: go forward")
        return True

    def switch_skin(self, skin_id=1):
        """
        模拟切换皮肤
        """
        print("##Mock: switch skin: {0}".format(skin_id))
        return True

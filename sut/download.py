# -*- coding: utf-8 -*-
"""
description: 
"""
__author__ = "cm"


import time


class DownloadBrowser(object):

    def download(self, url):
        # 模拟下载
        print("downloading {0}".format(url))
        time.sleep(1)
        print("")

    def exit(self):
        print("exit browser")

    def open_url(self, url):
        print("open url: {0}".format(url))

    def go_back(self):
        print("go back")

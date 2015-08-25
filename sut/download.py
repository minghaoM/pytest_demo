# -*- coding: utf-8 -*-
"""
description: 
"""
__author__ = "cm"


import time
from browser_base import BrowserBase


class DownloadBrowser(BrowserBase):

    def download(self, url):
        # 模拟下载
        print("##Mock: downloading {0}".format(url))
        time.sleep(1)
        print("download done.")

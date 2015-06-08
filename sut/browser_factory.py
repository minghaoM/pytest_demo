# -*- coding: utf-8 -*-
"""
description: 
"""
__author__ = "cm"


import config
from browser_base import BrowserBase
from download import DownloadBrowser
from mouse_gesture import MouseGestureBrowser


def get_browser(browser_name):
    browser = None
    options = {
        config.BROWSER_BASE: BrowserBase,
        config.BROWSER_DOWNLOAD: DownloadBrowser,
        config.BROWSER_MOUSE_GESTURE: MouseGestureBrowser
    }
    if browser_name in options:
        browser = options[browser_name]()
    return browser
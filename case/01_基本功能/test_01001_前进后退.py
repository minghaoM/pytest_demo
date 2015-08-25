# -*- coding: utf-8 -*-
"""
description: 测试浏览器的前进后退功能
"""
__author__ = "cm"


import pytest


@pytest.mark.priority(1)
def test_01001(fixture_browser_launch_exit):
    browser_obj = fixture_browser_launch_exit
    browser_obj.open_url("http://www.uc.cn")
    browser_obj.open_url("http://www.uc.cn/ucbrowser/download/")
    browser_obj.go_back()
    assert browser_obj.get_current_url("http://www.uc.cn") == "http://www.uc.cn"
    browser_obj.go_forward()
    assert browser_obj.get_current_url("http://www.uc.cn/ucbrowser/download/") == "http://www.uc.cn/ucbrowser/download/"


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])

# -*- coding: utf-8 -*-
"""
@description: pytest配置
"""
__author__ = "cm"


import pytest
from sut import browser_factory
from sut import config


def _browser_launch_exit(request, browser_name, does_clean_data=False):

    browser = browser_factory.get_browser(browser_name)
    if does_clean_data:
        # 模拟清理userdata的操作
        print("##Mock: clean user data")

    def fin():
        # 退出浏览器动作
        browser.close_browser()

    request.addfinalizer(fin)
    return browser


@pytest.fixture(scope="module")
def fixture_browser_launch_exit(request):
    """
    浏览器启动退出固件
    :param request:
    :return:
    """
    return _browser_launch_exit(request, config, does_clean_data=False)





@pytest.fixture(scope="module")
def fixture_browser_clean_launch(request):
    """
    浏览器启动前清除UserData
    :param request:
    :return:
    """
    return _browser_launch_exit(request, config, does_clean_data=True)


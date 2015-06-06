# -*- coding: utf-8 -*-
"""
@description:
"""
__author__ = "lina"


import pytest


@pytest.fixture(scope="module")
def fixture_browser_launch_exit(request):
    """
    浏览器启动退出固件
    :param request:
    :return:
    """
    tin.system.kill_process("UCBrowser.exe")
    if does_clean_data:
        time.sleep(1)
        uclib.clean_userdata()
    if load_bookmarks:
        tin.browser.copy_dir()
    browser = tin.browser_factory.get_browser(browser_constant)

    def fin():
        # 退出浏览器动作
        browser.close_browser()

    request.addfinalizer(fin)
    return browser



@pytest.fixture(scope="module")
def fixture_browser_clean_launch(request):
    """
    浏览器启动前清除UserData
    :param request:
    :return:
    """
    return _browser_launch_exit(request, tin.constant.CLASS_UC, does_clean_data=True)


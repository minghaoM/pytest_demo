# -*- coding: utf-8 -*-
"""
@description: pytest配置
"""
__author__ = "cm"


import pytest
from sut import browser_factory
from sut import config
import demo_util
from html_report import HtmlReport
from txt_report import TxtReport


def pytest_addoption(parser):
    """
    增加-P参数，标识要执行testcase的优先级
    增加测试结果输出参数
    """
    demo_util.pause_show_info("pytest_addoption in conftest")
    has_p = False
    for options in parser._anonymous.options:
        if "-P" in options._short_opts:
            has_p = True
    if not has_p:
        parser.addoption("-P", type=int, metavar="NAME",
            help="only run tests equal or lower than the priority")

    group_report = parser.getgroup("report output")
    group_report.addoption('--html-result', action="store",
           dest="html_result", type=bool, metavar="NAME", default=False,
           help="output html result.")
    group_report.addoption('--txt-result', action="store",
           dest="txt_result", type=bool, metavar="NAME", default=False,
           help="output txt result.")


def pytest_configure(config):
    """
    注册plugin
    """
    demo_util.pause_show_info("pytest_configure in conftest")
    # 根据传参注册相应的plugin
    enable_html_report = config.option.html_result
    enable_txt_report = config.option.txt_result
    if enable_html_report and not hasattr(config, 'slaveinput'):
        config.html_report = HtmlReport()
        config.pluginmanager.register(config.html_report)
    if enable_txt_report and  not hasattr(config, 'slaveinput'):
        config.txt_report = TxtReport()
        config.pluginmanager.register(config.txt_report)


def pytest_unconfigure(config):
    demo_util.pause_show_info("pytest_unconfigure in conftest")
    html_report = getattr(config, 'html_report', None)
    txt_report = getattr(config, 'txt_report', None)
    if html_report:
        del config.html_report
        config.pluginmanager.unregister(html_report)
    if txt_report:
        del config.txt_report
        config.pluginmanager.unregister(txt_report)


def pytest_runtest_setup(item):
    """
    执行priority小于等于传入-P参数的testcase
    -P 1:只执行优先级为1的testcase
    -P 2:执行优先级为1或2的testcase
    :param item:
    :return:
    """
    print("\n--{0}".format(item.name))
    demo_util.pause_show_info("pytest_runtest_setup in conftest")
    p_marker = item.get_marker("priority")
    if p_marker is not None:
        p = p_marker.args[0]
        print("*"*77)
        print("case priority:{0}".format(p))
        try:
            run_p = item.config.getoption("-P")
            # 默认优先级为3，执行所有优先级为1,2,3的testcase
            if run_p is None:
                run_p = 3
            print("run priority:{0}".format(run_p))
        except AttributeError:
            return
        if p > run_p:
            pytest.skip("test case priority:{0} is lower than run priority:{1}".format(run_p, p))


def _browser_launch_exit(request, browser_name, does_clean_data=False):

    browser = browser_factory.get_browser(browser_name)
    browser.launch()
    if does_clean_data:
        # 模拟清理userdata的操作
        print("##Mock: clean user data")

    def fin():
        # teardown动作退出浏览器动作
        browser.exit()

    request.addfinalizer(fin)
    return browser


@pytest.fixture(scope="module")
def fixture_browser_launch_exit(request):
    """
    浏览器启动退出固件
    :param request:
    :return:
    """
    return _browser_launch_exit(request, config.BROWSER_BASE, does_clean_data=False)


@pytest.fixture(scope="module")
def fixture_browser_clean_launch(request):
    """
    浏览器启动前清除UserData
    :param request:
    :return:
    """
    return _browser_launch_exit(request, config.BROWSER_BASE, does_clean_data=True)


@pytest.fixture(scope="module")
def fixture_download_launch_exit(request):
    """
    浏览器启动退出固件
    :param request:
    :return:
    """
    return _browser_launch_exit(request, config.BROWSER_DOWNLOAD, does_clean_data=False)


@pytest.fixture(scope="module")
def fixture_download_clean_launch(request):
    """
    浏览器启动前清除UserData
    :param request:
    :return:
    """
    return _browser_launch_exit(request, config.BROWSER_DOWNLOAD, does_clean_data=True)


@pytest.fixture(scope="module")
def fixture_gesture_launch_exit(request):
    """
    浏览器启动退出固件
    :param request:
    :return:
    """
    return _browser_launch_exit(request, config.BROWSER_MOUSE_GESTURE, does_clean_data=False)


@pytest.fixture(scope="module")
def fixture_gesture_clean_launch(request):
    """
    浏览器启动前清除UserData
    :param request:
    :return:
    """
    return _browser_launch_exit(request, config.BROWSER_MOUSE_GESTURE, does_clean_data=True)


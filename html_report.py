# -*- coding: utf-8 -*-
"""
@description: html report plugin
"""
__author__ = "cm"

import demo_util
from report_base import ReportBase


class HtmlReport(ReportBase):
    def pytest_sessionfinish(self):
        """
        所有case执行完毕后，生成html格式测试报告
        :return:
        """
        demo_util.pause_show_info("pytest_sessionfinish in HtmlReport")
        demo_util.gen_report_file("html_report.txt", "html test")



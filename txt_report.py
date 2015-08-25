# -*- coding: utf-8 -*-
"""
@description: txt report plugin
"""
__author__ = "cm"


import demo_util
from report_base import ReportBase


class TxtReport(ReportBase):
    def pytest_sessionfinish(self):
        """
        所有case执行完毕后，生成html格式测试报告
        :return:
        """
        demo_util.pause_show_info("pytest_sessionfinish in TxtReport")
        demo_util.gen_report_file("txt_report.txt", "txt test")

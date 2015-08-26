# -*- coding: utf-8 -*-
"""
@description: txt report plugin
"""
__author__ = "cm"


import os
import demo_util
from report_base import ReportBase


class TxtReport(ReportBase):
    def pytest_sessionfinish(self):
        """
        所有case执行完毕后，生成html格式测试报告
        :return:
        """
        demo_util.pause_show_info("pytest_sessionfinish in TxtReport")
        file_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(file_dir, "txt_report.txt")
        demo_util.gen_report_file(file_path, "txt test")

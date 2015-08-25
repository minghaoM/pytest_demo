# -*- coding: utf-8 -*-
"""
@description: report base
"""
__author__ = "cm"


import _pytest
import time
import demo_util


class ReportBase(object):
    def __init__(self):
        self.tests = []
        self.failed_tests = []
        self.passed = self.skipped = 0
        self.failed = self.errors = 0

    def append(self, report):
        self.tests.append(report)

    def append_pass(self, report):
        self.passed += 1
        self.append(report)

    def append_failure(self, report):
        self.failed += 1
        self.append(report)
        self.failed_tests.append(report)

    def append_error(self, report):
        self.errors += 1
        self.append(report)
        self.failed_tests.append(report)

    def append_skipped(self, report):
        self.skipped += 1
        self.append(report)

    def pytest_runtest_makereport(self, item, call):
        demo_util.pause_show_info("pytest_runtest_makereport in {0}".format(self))
        report = _pytest.runner.pytest_runtest_makereport(item, call)
        if "__author__" not in dir(item.module):
            report.keywords["author"] = "unknown"
        else:
            report.keywords["author"] = item.module.__author__.decode("utf8").encode("gbk")
        return report

    def pytest_runtest_logreport(self, report):
        """
        每个testcase执行完的report处理
        """
        demo_util.pause_show_info("pytest_runtest_logreport in {0}".format(self))
        if report.passed:
            if report.when == "call": # ignore setup/teardown
                self.append_pass(report)
        elif report.failed:
            if report.when != "call":
                self.append_error(report)
            else:
                self.append_failure(report)
        elif report.skipped:
            self.append_skipped(report)

    def pytest_sessionstart(self):
        demo_util.pause_show_info("pytest_sessionstart in {0}".format(self))
        self.suite_start_time = time.time()


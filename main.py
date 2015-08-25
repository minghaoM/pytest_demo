# -*- coding: utf-8 -*-
"""
@description:
"""
__author__ = "cm"


import argparse
import os
import pytest


DEFAULT_CASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "case")


def run():
    parser = argparse.ArgumentParser(description="运行UI自动化测试用例".decode("utf8"))
    parser.add_argument("--casepath", default=DEFAULT_CASE_PATH,
                        help="测试用例的执行目录，不设置时默认执行case目录下全部用例".decode("utf8"))
    parser.add_argument("-P", "--priority", type=int, default=3,
                        help="运行测试用例的优先级(1,2,3)，不设置默认执行全部优先级的用例".decode("utf8"))
    parser.add_argument("--html-result", action="store",
                        dest="html_result", type=bool, metavar="NAME", default=False,
                        help="输出html报表".decode("utf8"))
    parser.add_argument("--txt-result", action="store",
                        dest="txt_result",  type=bool, metavar="NAME", default=False,
                        help="输出txt报表".decode("utf8"))
    args = parser.parse_args()
    case_path_str = args.casepath.replace("\\", "\\\\")
    priority_str = " -P {0}".format(args.priority)
    html_report_str = ""
    txt_report_str = ""
    if args.html_result:
        html_report_str = " --html-result True"
    if args.txt_result:
        txt_report_str = " --txt-result True"
    pytest_str = r" {case_path}{priority}{html_report}{txt_report} -s --clearcache".format(
        case_path=case_path_str, priority=priority_str,
        html_report=html_report_str, txt_report=txt_report_str
    )
    print("py.test {0}".format(pytest_str))
    pytest.main(pytest_str)


if __name__ == "__main__":
    run()

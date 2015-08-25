# -*- coding: utf-8 -*-
"""
@description:
"""
__author__ = "cm"


import os
import time


def pause_show_info(info):
    print("=" * 70)
    print("=== {0}".format(info))
    time.sleep(1)


def gen_report_file(file_name, content):
    """
    生成测试报告文件
    :param content: 文件内容
    :return:
    """
    file_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_dir, file_name)
    print("outputing report:{0}".format(file_path))
    with open(file_path, "w") as f:
        f.write(content)
    return True

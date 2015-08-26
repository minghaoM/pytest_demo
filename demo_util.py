# -*- coding: utf-8 -*-
"""
@description:
"""
__author__ = "cm"


import platform
import os
import time


def gen_report_file(file_path, content):
    """
    生成测试报告文件
    :param content: 文件内容
    :return:
    """
    print("outputing report:{0}".format(file_path))
    with open(file_path, "w") as f:
        f.write(content)
    return True


def pause_show_info(info):
    print("=" * 70)
    print("=== {0}".format(info))
    time.sleep(1)


def is_triangle(tri_tuple):
    s1, s2, s3 = tri_tuple
    for i in tri_tuple:
        if i <= 0:
            return False
    if s1 + s2 <= s3:
        return False
    if abs(s1 - s2) >= s3:
        return False
    return True


def get_os_bit():
    """
    获取操作系统位数信息，32bit或64bit
    """
    os_bit = platform.machine()
    if os_bit.lower() == "amd64":
        bit_str = "64bit"
    elif os_bit.lower() == "x86":
        bit_str = "32bit"
    else:
        bit_str = os_bit
    return bit_str

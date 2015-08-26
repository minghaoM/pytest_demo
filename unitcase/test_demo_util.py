# -*- coding: utf-8 -*-
"""
description: demo_util单元测试
"""
__author__ = "lina"


import sys
import pytest
import os
import platform
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import demo_util


def test_gen_report_file(tmpdir):
    print("***run case gen_report_file")
    out_dir = str(tmpdir.mkdir("output").realpath())
    output_file = os.path.join(out_dir, "test")
    content = "test abc"
    demo_util.gen_report_file(output_file, content)
    assert os.path.isfile(output_file)
    with open(output_file) as f:
        result_content = f.read()
    assert result_content == content


@pytest.mark.parametrize("input_par, expected", [
    ((2, 3, 4), True),
    ((1, 2, 3), False),
    ((-2, -3, 4), False),
    ((0, 0, 0), False)
])
def test_is_triangle(input_par, expected, fixture_browser_launch_exit):
    print("***run case is_triangle")
    assert demo_util.is_triangle(input_par) == expected


def test_get_os_bit(monkeypatch):
    print("***run case get_os_bit")
    monkeypatch.setattr(platform, "machine", lambda : "x86")
    assert demo_util.get_os_bit() == "32bit"
    monkeypatch.setattr(platform, "machine", lambda : "amd64")
    assert demo_util.get_os_bit() == "64bit"


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])

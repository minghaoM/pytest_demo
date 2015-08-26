# -*- coding: utf-8 -*-
"""
description: 
"""
__author__ = "sven"


import pytest


@pytest.mark.priority(2)
def test_01002(fixture_browser_launch_exit):
    print("***run case 01002")
    assert True


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])

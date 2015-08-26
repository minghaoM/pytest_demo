# -*- coding: utf-8 -*-
"""
description: 
"""
__author__ = "jugg"


import pytest


@pytest.mark.priority(3)
def test_01004(fixture_browser_launch_exit):
    print("***run case 01004")
    assert True


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])

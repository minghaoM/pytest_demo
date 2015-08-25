# -*- coding: utf-8 -*-
"""
description: 
"""
__author__ = "sa"


import pytest


@pytest.mark.priority(1)
def test_03001(fixture_gesture_clean_launch):
    print("***run case 03001")
    assert True


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])

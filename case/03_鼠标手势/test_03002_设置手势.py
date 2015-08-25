# -*- coding: utf-8 -*-
"""
description: 
"""
__author__ = "sa"


import pytest


@pytest.mark.priority(2)
def test_02002(fixture_gesture_clean_launch):
    print("***run case 03002")
    assert True


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])

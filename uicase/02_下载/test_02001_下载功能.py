# -*- coding: utf-8 -*-
"""
description: 
"""
__author__ = "lina"


import pytest


@pytest.mark.skipif(True, reason="just test")
@pytest.mark.priority(1)
def test_02001(fixture_download_launch_exit):
    print("***run case 02001")
    assert True


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])

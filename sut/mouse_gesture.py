# -*- coding: utf-8 -*-
"""
@description:
"""
__author__ = "sa"


from browser_base import BrowserBase

GESTURE_VAL_FORWARD = 1
GESTURE_VAL_BACK = 2

GESTURE_TYPE_1 = 1
GESTURE_TYPE_2 = 2


class MouseGestureBrowser(BrowserBase):

    def do_gesture(self, gesture_type):
        """
        模拟打开新标签
        """
        print("##Mock: do gesture: {0}".format(gesture_type))
        return True

    def set_gesture(self, gesture_type, gesture_val):
        """
        模拟打开新标签
        """
        print("##Mock: set gesture")
        return True


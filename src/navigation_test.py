#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gs_navigation import NavigationManager
from gs_board import BoardManager

rospy.init_node("navigation_test_node")
board=BoardManager()
navigation=NavigationManager()
once=False

while not rospy.is_shutdown():
    if(board.runStatus()):
        print(navigation.navigationSystem())
        print(navigation.globalPosition())
        print(navigation.localPosition())
        print(navigation.optVelocity())
        once=True
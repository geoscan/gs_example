#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gs_board import BoardManager
from time import sleep

rospy.init_node("board_test_node")
board = BoardManager()

run = True

while not rospy.is_shutdown() and run:
    if board.runStatus():
        print("start of programm")
        print(board.boardNumber())
        sleep(2)
        print(board.time())
        sleep(1)
        print(board.uptime())
        sleep(1)
        print(board.flightTime())
        print("end of programm")
        run = False
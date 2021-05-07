#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gs_flight import FlightController, CallbackEvent
from gs_board import BoardManager
from gs_navigation import NavigationManager
from time import sleep

rospy.init_node("flight_global_test_node")
gps = NavigationManager().gps
start_pos = gps.position()

coordinates = [
    [start_pos[0], start_pos[1] + 0.00001, 20],
    [start_pos[0] + 0.00001, start_pos[1] + 0.00001, 20],
    [start_pos[0] + 0.00001, start_pos[1], 20],
    [start_pos[0], start_pos[1], 20],
]

run = True
position_number = 0

def callback(event):
    global ap
    global run
    global coordinates
    global position_number

    event = event.data
    if event == CallbackEvent.ENGINES_STARTED:
        print("engine started")
        ap.takeoff()
    elif event == CallbackEvent.TAKEOFF_COMPLETE:
        print("takeoff complite")
        position_number = 0
        print(f"point {position_number} start")
        ap.goToPoint(coordinates[position_number][0], coordinates[position_number][1], coordinates[position_number][2])
    elif event == CallbackEvent.POINT_REACHED:
        print("point {} reached".format(position_number))
        position_number += 1
        if position_number < len(coordinates):
            ap.goToPoint(coordinates[position_number][0], coordinates[position_number][1], coordinates[position_number][2])
        else:
            ap.landing()
    elif event == CallbackEvent.COPTER_LANDED:
        print("finish programm")
        run = False

board = BoardManager()
ap = FlightController(callback)
once = False

while not rospy.is_shutdown() and run:
    if board.runStatus() and not once:
        print("start programm")
        ap.preflight()
        once = True
    pass

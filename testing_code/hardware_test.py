#!/usr/bin/env python3

import time

import payload

def main():
    bagpiper = payload.Payload()
    print("Payload initialized")

    # bagpiper.rot_left()
    # print("Rotated left")
    # time.sleep(1)
    # bagpiper.rot_right()
    # print("Rotated left")
    # time.sleep(1)

    # bagpiper.rot_up()
    # print("Rotated up")
    # time.sleep(1)
    # bagpiper.rot_down()
    # print("Rotated down")
    # time.sleep(1)

    print("spinning")
    bagpiper.rot_motor()
    print("spinning")
    bagpiper.rot_motor()
    print("spinning")
    bagpiper.rot_motor()
    print("spinning")
    bagpiper.rot_motor()
    
main()
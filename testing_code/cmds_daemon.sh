#!/bin/bash
tail -f /home/pi/multimon_pipe | while read -r line; do python3 /home/pi/Desktop/wServo.py "$line"; done

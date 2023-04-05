# Author: Josh Huang
# main script that runs upon pi turn on

from datetime import datetime
import time
from imu import IMU
from servo0 import Servo0
from servo1 import Servo1
from camera import Camera
from radioParser import RadioParser
from dc import DC
import math
import RPi.GPIO as GPIO

debug = True
vars = {}
if debug:
    vars = dict(launch_accel=11, landing_delta_accel=0.1, landing_wait_time=5)
else:
    vars = dict(launch_accel=20, landing_delta_accel=0.1, landing_wait_time=180)

#region initialize components
imu = IMU()
s0 = Servo0()
s1 = Servo1()
dc = DC()
radioParser = RadioParser()
cam = Camera()

LOGNAME = "bagpiper-log.txt"

#endregion
    
def main():
    #region phase1 on pad
    GPIO.setup(21, GPIO.OUT)
    beep()
    
    log_info("Waiting for launch")
    a = 0.99
    x,y,z = imu.getAccel()
    prev_mag = magnitude(x,y,z)
    while True:
        x,y,z = imu.getAccel()
        mag = magnitude(x,y,z)
        mag = prev_mag*a + mag*(1-a)

        if (mag > vars['launch_accel']):
            log_info("Launch!")
            break
            
        prev_mag = mag
        time.sleep(.01)
    #endregion
        
    #region phase2 launched/detect land
    beep()
    beep()
    x,y,z = imu.getAccel()
    prev_mag = magnitude(x,y,z)
    land_time = 0
    while True:
        x,y,z = imu.getAccel()
        mag = magnitude(x,y,z)
        mag = mag*a + prev_mag*(1-a)
        
        if (abs(mag - prev_mag) < vars['landing_delta_accel']):
            if (land_time == 0):
                land_time = datetime.now()
            if (datetime.now() - land_time).total_seconds() > vars['landing_wait_time']:
                log_info("Landed!")
                break
        else:
            land_time = 0
        
        prev_mag = mag
        time.sleep(.05)
    #endregion
        
    #region phase3 deploy
    beep()
    beep()
    beep()
    theta_DC,theta_0 = imu.GetAdjustments()
    log_info(str(theta_DC) + ', ' + str( theta_0))
    
    turns = 0
    turn_time = datetime.now()
    # while True:
    #     if turns >= 7 or (datetime.now() - turn_time).total_seconds() > 20:
    #         print("break turn")
    #         break
    #     if abs(theta_DC) < 5:
    #         turns += 1
    #         while abs(theta_DC) < 5:
    #             time.sleep(.1)
    # dc.go()
    # time.sleep(7)
    # while True:
    #     theta_DC,theta_0 = imu.GetAdjustments()
    #     if abs(theta_DC) < 5:
    #         dc.stop()
    #         break
        
    s0.rotate(theta_0)
    log_info("Deployed!")
    #endregion
    
    #region phase4 camera commands
    beep()
    beep()
    beep()
    beep()
    conductExperiemnt()
        
    #endregion
    
    #???: ability to re-adjust payload if IMU detects payload has shifted?
    
def conductExperiemnt(debug = False):
    # python -c 'import main; main.conductExperiemnt(True)'
    completed_cmds_lst = []
    start_read = datetime.now()
    while True:
        commands_lst = radioParser.parser(debug)
        for cmds in commands_lst:
            for completed_cmds in completed_cmds_lst:
                if cmds == completed_cmds:
                    commands_lst.remove(cmds)
        print(f"commands_lst: {commands_lst}")
        # if commands_lst:
        if not debug:
            log_info(str(commands_lst))
        for cmds in commands_lst:
            completed_cmds_lst.append(cmds)
            for cmd in cmds:
                print(cmd)
                # if (cmd == "A1"): # Turn camera 60º to the right
                #     s1.rotate(60)
                # elif (cmd == "B2"): #Turn camera 60º to the left
                #     s1.rotate(-60)
                # elif (cmd == "C3"): # Take picture
                #     cam.capture("PDF")
                # elif (cmd == "D4"): # Change camera mode from color to grayscale
                #     pass
                # elif (cmd == "E5"): # Change camera mode back from grayscale to color 
                #     pass
                # elif (cmd == "F6"): # Rotate image 180º (upside down).
                #     pass
                # elif (cmd == "G7"): # Special effects filter (Apply any filter or image distortion you want and state what filter or distortion was used)
                #     pass
                # elif (cmd == "H8"): # Remove all filters.
                #     pass
        
        if (datetime.now() - start_read).total_seconds() > 300:
            log_info("Timed out")
            break
        time.sleep(10)


def magnitude(x,y,z):
    return math.sqrt(x*x + y*y + z*z)

def beep(time_high=0.5, time_low=0.2):
    '''beeps the amount specified, or else does the default beep'''
    GPIO.output(21, GPIO.HIGH)
    time.sleep(time_high)
    GPIO.output(21, GPIO.LOW)
    time.sleep(time_low)
    
def log_info(message):
    '''logs message given AND THEN CLOSES THE FILE TO FLUSH THE BUFFER'''
    with open(LOGNAME, 'a+') as log:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{now}: {message}\n")
        print(message)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # instead of quietly erroring, write the error to a file, beep 
        # like hell, and then still attempt to raise the error
        log_info(str(e))
        for i in range(10):
            beep(0.1, 0.1)
        raise(e)

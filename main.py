# Author: Josh Huang
# main script that runs upon pi turn on
import time
from imu import IMU
from servo0 import Servo0
from servo1 import Servo1
from camera import Camera
from radioParser import RadioParser
import math

debug = False

def main():
    #region phase 1
    
    #region initialize components
    imu = IMU()
    s0 = Servo0()
    s1 = Servo1()
    # TODO initialize DC motor class
    radioParser = RadioParser()
    cam = Camera()
    #endregion
    
    a = 0.9
    prev_mag = magnitude(imu.getAccel())
    while True:
        mag = magnitude(imu.getAccel())
        mag = mag*a + prev_mag*(1-a)
        prev_mag = mag

        print(mag)
        
        
        
        
        
    #endregion
    
    theta_DC,theta_0 = imu.GetAdjustments()
    
    #region tests
    if debug:
        s0.test()
        s1.test()
        # TODO hardware test DC motor
        # cam.capture("class-test")
    #endregion
    
    # TODO: get servo accelerations and determine if rocket has landed or has moved during payload deployment
    
    #region deployment
    
    print(theta_DC, theta_0)
    # TODO: use DC class to make adjustments based on imu
    s0.rotate(theta_0)

    #endregion
    
    #region camera commands
    # TODO use radio class to get a list of commands to execute
    print(radioParser.parser())
    # IDEA: use generator to iterate through commands, see yield and generator in python
    # for cmd in commands.
    # print(radioParser.cmd_lst)
    # radioParser.receive()
    # print(radioParser.cmd_lst)
    
    s1.rotate(90)
    s1.rotate(-90)
    # s1.rotate(180)
    s1.rotate(-45)
    s1.rotate(45)
    cam.capture()

    # TODO: use camera class to take pictures and do filters
    #endregion
    
    #???: ability to re-adjust payload if IMU detects payload has shifted?

def magnitude(x,y,z):
    return math.sqrt(x*x + y*y + z*z)

if __name__ == "__main__":
    main()
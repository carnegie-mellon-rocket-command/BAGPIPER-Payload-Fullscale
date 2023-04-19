# Author: Josh Huang

from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory
import os

factory = PiGPIOFactory()

servo = Servo(24, pin_factory=factory) #original pin 24
servo.value = None

#region settings
ccw = .115
cw = -.25
t_ratio = .45/90
#endregion

class Servo1:
    def __init__(self):
        self.left_cnt = 0
        self.right_cnt = 0
        print("servo 1 initiated")
        
    def test(self):
        '''
        Testing that the servo works by turning it around a bit
        '''
        print('testing S1')
        servo.value = cw
        time.sleep(0.5)
        servo.value = ccw
        time.sleep(0.5)
        # servo.value = ccw
        # time.sleep(0.45)
        self.stop()
    
    def rotate(self, degrees):
        '''
        Rotates the servo 1 by a number of degrees
        '''
        reset = False
        degrees = -degrees
                
        if degrees > 0: #ccw, right
            self.right_cnt += 1
            if self.right_cnt >= 7:
                reset = True
                servo.value = cw
                self.right_cnt = 0
            else:
                servo.value = ccw
        else: # cw, left
            self.left_cnt += 1
            if self.left_cnt >= 7:
                reset = True
                servo.value = ccw
                self.left_cnt = 0
            else:
                servo.value = cw
        if reset:
            time.sleep(t_ratio * abs(360))
        else:  
            time.sleep(t_ratio * abs(degrees))
        self.stop()
       
    def stop(self):
        servo.value = None
        time.sleep(1)

def test():
    # python -c 'import servo1; servo1.test()'
    s1 = Servo1()
    # s1.test()
    servo.value = -1
    time.sleep(0.2)
    s1.stop()
# Author: Josh Huang

from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory
import os

factory = PiGPIOFactory()

servo = Servo(24, pin_factory=factory)
servo.value = None

#region settings
ccw = .115
cw = -.2
t_ratio = .45/90
#endregion

class Servo1:
    def __init__(self):
        print("servo 1 initiated")
        
    def test(self):
        '''
        Testing that the servo works by turning it around a bit
        '''
        servo.value = cw
        time.sleep(0.5)
        servo.value = ccw
        time.sleep(0.5)
        servo.value = ccw
        time.sleep(0.45)
        self.stop()
    
    def rotate(self, degrees):
        '''
        Rotates the servo 1 by a number of degrees
        '''
        if degrees > 0: #ccw
            servo.value = ccw
        else:
            servo.value = cw
            print("negative run")
        time.sleep(t_ratio * abs(degrees))
        self.stop()
       
    def stop(self):
        servo.value = None
        time.sleep(1)


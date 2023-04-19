# Author: Josh Huang

from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO
import os

factory = PiGPIOFactory()
servo = Servo(24, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

# limit_angle = -40/90 # angle where servo hits camera platform
# adjustment_angle = -23 # angle from min servo to horizontal


servo.value = None # prevents servo from moving upon init

class Servo1:
    def __init__(self):
        self.angle = [0, 60, 120, 180, 240, 300]
        self.position = 2
        print("servo 1 initiated")
        
    def test(self):
        '''
        Test that the servo runs by rotating the servo back and forth
        '''
        print('testing S0')
        servo.mid()
        time.sleep(1)
        servo.max() 
        time.sleep(1)
        servo.min() 
        time.sleep(1)
        servo.max() 
        time.sleep(1)
        servo.mid() 
        time.sleep(1)
        self.stop()
    
    def rotate(self):
        '''
        Rotates the base servo 0 by a number of degrees, degrees given by IMU in main class
        '''
        # adjust rotation for angle of servo arm and get it to servo readable scale
        C = self.angle[self.position % len(self.angle)]/300
        print(f"angle: {self.angle}, C: {C}")
        rot = (C * -1) + ((1-C) * 1) # convex combination
        
        # limit rot from limit_angle to 1
        # rot = limit_angle if rot < limit_angle else 1 if rot > 1 else rot
        servo.value = rot
        self.stop()
        
    def right(self):
        self.position += 1
        self.rotate()
    
    def left(self):
        self.position -= 1
        self.rotate()
       
    def stop(self):
        '''
        stops the servo from drawing more power, has sleep time before stop to allow time to move rotate servo
        '''
        time.sleep(1)
        servo.value = None
        
    def reset(self):
        self.position = 2
        self.rotate()

s1 = Servo1()
def test(pos=2):
    # python -c 'import servo1; servo1.test()'
    # s1.left()
    s1.position = pos
    s1.rotate()
    
    # servo.min()
    # servo.value = 1
    # time.sleep(1)

    s1.stop()
    
def reset():
    s1 = Servo1()
    s1.reset()
# Author: Josh Huang

from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO
import os

factory = PiGPIOFactory()
servo = Servo(23, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

limit_angle = -40/90 # angle where servo hits camera platform
adjustment_angle = -23 # angle from min servo to horizontal
servo.value = None # prevents servo from moving upon init

class Servo0:
    def __init__(self):
        print("servo 0 initiated")
        
    def test(self):
        '''
        Test that the servo runs by rotating the servo back and forth
        '''
        servo.mid()
        time.sleep(1)
        servo.max() 
        time.sleep(1)
        self.stop()
    
    def rotate(self, degrees):
        '''
        Rotates the base servo 0 by a number of degrees, degrees given by IMU in main class
        '''
        # adjust rotation for angle of servo arm and get it to servo readable scale
        rot = -degrees + adjustment_angle
        rot = rot/90
        
        # limit rot from limit_angle to 1
        rot = limit_angle if rot < limit_angle else 1 if rot > 1 else rot
        servo.value = rot
        self.stop()
       
    def stop(self):
        '''
        stops the servo from drawing more power, has sleep time before stop to allow time to move rotate servo
        '''
        time.sleep(1)
        servo.value = None

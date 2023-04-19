# author: Josh Huang

import time
import RPi.GPIO as GPIO

class Buzzer():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    
    def __init__(self):
        print("buzzer initiated")
        
    def beep(self, on_t = .2, off_t = .2, n=1):
        for i in range(0, n):
            GPIO.output(21, GPIO.HIGH)
            time.sleep(on_t)
            GPIO.output(21, GPIO.LOW)
            time.sleep(off_t)
        
import RPi.GPIO as GPIO
import time

class DC:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        print("DC initiated")
    
    def go(self):
        GPIO.output(12, GPIO.HIGH)
        
    def stop(self):
        GPIO.output(12, GPIO.LOW)
        
dc = DC()
dc.go()
time.sleep(3)
dc.stop()

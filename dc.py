import RPi.GPIO as GPIO
import time

out = 25 #previously 12

class DC:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(out, GPIO.OUT)
        print("DC initiated")
    
    def go(self):
        GPIO.output(out, GPIO.HIGH)
        
    def stop(self):
        GPIO.output(out, GPIO.LOW)
        
def test():
    # python -c 'import dc; dc.test()'
    dc = DC()
    dc.go()
    time.sleep(7)
    dc.stop()
    time.sleep(7)


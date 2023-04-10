import RPi.GPIO as GPIO
import time

out = 12 #previously 12

class DC:
    def __init__(self, pin=12):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        print("DC initiated")

    def extend(self):
        
        GPIO.output(self.pin, GPIO.HIGH)
        
    def stop(self):
        GPIO.output(self.pin, GPIO.LOW)
        
def test():
    # python -c 'import dc; dc.test()'
    dc = DC()
    dc.extend()
    time.sleep(4)
    dc.stop()
    


import RPi.GPIO as GPIO
import time

out = 12 #previously 12

class DC:
    def __init__(self, forward=12, back=16):
        self.forward = forward
        self.back = back

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.forward, GPIO.OUT)
        GPIO.setup(self.back, GPIO.OUT)

        print("DC initiated")
    
    def go(self):
        GPIO.output(self.forward, GPIO.HIGH)
        GPIO.output(self.back, GPIO.LOW)

    def backward(self):
        GPIO.output(self.forward, GPIO.LOW)
        GPIO.output(self.back, GPIO.HIGH)
        
    def stop(self):
        GPIO.output(self.forward, GPIO.LOW)
        GPIO.output(self.back, GPIO.LOW)
        
def test():
    # python -c 'import dc; dc.test()'
    dc = DC()
    dc.go()
    time.sleep(7)
    dc.stop()
    time.sleep(7)


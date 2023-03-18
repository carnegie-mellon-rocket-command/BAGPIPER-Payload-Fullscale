from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO

factory = PiGPIOFactory()

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(24,GPIO.OUT)
# servo1 = GPIO.PWM(24,50)
# servo1.start(0)
# servo1.ChangeDutyCycle(10)

#servo=Servo(23, pin_factory=factory)
# servo=Servo(24)
servo = Servo(23, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
# servo = Servo(8, min_pulse_width=0.5/1000, max_pulse_width=15/1000, pin_factory=factory)
servo.value = -0.25570728169805046
# servo.max()
time.sleep(2)
servo.value = None

# servo.mid()
# time.sleep(3)
# servo.max()
# time.sleep(3)
# servo.mid()
# time.sleep(3)
# servo.max()
# time.sleep(3)
# servo.max()
# time.sleep(3)

import RPi.GPIO as GPIO
import time

class Payload:
    def __init__(self, servo_0=23, servo_1=25, dc_motor=8, buzz=21):
        # self.servo_0_pin = servo_0
        # self.duty_0 = 0
        # self.servo_1_pin = servo_1
        # self.duty_1 = 0
        self.dc_motor = dc_motor
        self.buzz = buzz

        GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.servo_0,GPIO.OUT)
        # GPIO.setup(self.servo_1,GPIO.OUT)

        # self.servo_0 = GPIO.PWM(self.servo_0_pin,50)
        # self.servo_1 = GPIO.PWM(self.servo_1_pin,50)

        GPIO.setup(self.dc_motor,GPIO.OUT)

        GPIO.setup(self.buzz, GPIO.OUT)
        GPIO.output(self.buzz, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(self.buzz, GPIO.LOW)
        time.sleep(.2)
        GPIO.output(self.buzz, GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(self.buzz, GPIO.LOW)
        time.sleep(.2)
        GPIO.output(self.buzz, GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(self.buzz, GPIO.LOW)

    def rot_left(self):
        self.duty_1 += 4
        self.servo_1.ChangeDutyCycle(self.duty_1)

    def rot_right(self):
        self.duty_1 -= 4
        self.servo_1.ChangeDutyCycle(self.duty_1)
    
    def rot_up(self):
        self.duty_0 += 4
        self.servo_0.ChangeDutyCycle(self.duty_0)
    
    def rot_down(self):
        self.duty_0 -= 4
        self.servo_0.ChangeDutyCycle(self.duty_0)

    def rot_motor(self):
        GPIO.output(self.dc_motor, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.dc_motor, GPIO.LOW)

    def take_pic(self):
        # take pic
        # return pic
        pass
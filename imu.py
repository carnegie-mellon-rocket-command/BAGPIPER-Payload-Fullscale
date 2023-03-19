# Author: Josh Huang

import math
import board
from adafruit_lsm6ds.ism330dhcx import ISM330DHCX

accels = (0,0,0)
class IMU:
    
    def __init__(self):
        self.i2c = board.I2C()
        self.sensor = ISM330DHCX(self.i2c)
        print("imu initiated")

    def GetAdjustments(self):
        '''
        Returns the rotation in degrees needed to adjust the payload camera to be upright
        Returns in a list of [z, x], where z is rotation of DC motor and x is rotation of servo 0 (base)
        
        GetAdjustments -> [-30.9, 12]
        GetAdjustments -> [50.9, -90.2]
        GetAdjustments -> [-180, 34.2]
        '''
        [acc_x, acc_y, acc_z] = self.sensor.acceleration

        # offset z by 180 degrees to face up
        offset_z = -math.pi + math.radians(13)
        # Angle along the Z-Axis of rotation needed to point up.
        theta_z = math.degrees(math.atan2(acc_x, acc_y) + offset_z)
        # correct for negative adjustment
        if (theta_z < -180):
            theta_z = theta_z + 360

        # Uses the distance formula (a^2 + b^2 = c^2) to calculate length of "c"
        # between the acceleration values of x and y. This provides a constant
        # value when the payload is rotated along the Z-axis.
        c = math.sqrt(acc_x**2 + acc_y**2)

        # Determines the direction of the rotation since the distance formula only
        # outputs positive values.
        direction = 1 if acc_y < 0 else -1

        # Offset of 90 degrees since we actually want the payload to lay flat.
        offset_x = -math.pi / 2
        # between -90 and +90 is what we want to work with, otherwise tell DC motor to turn over

        theta_x = math.degrees(math.atan2(c * direction, acc_z) + offset_x)
        return [theta_z, theta_x]
    
    def isLaunch(self):
        '''
        use IMU measurements to detect when the rocket has launched off the pad
        '''
        [x,y,z] = self.sensor.acceleration
        return [x,y,z]
        
        pass
    
    def hasLanded(self):
        '''
        use IMU meausrements to detect when the rocket has landed
        '''
        pass
    
    def getAccel(self):
        (x,y,z) = self.sensor.acceleration
        return (x,y,z)

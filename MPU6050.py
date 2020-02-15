'''
the class of MPU6050
author: object123
time: 2020-1-25
function: init(set the setting of MPU6050)
          getAccel(get the acceleration of X.Y.Z )
          getGyro(get the angular velocity of X.Y.Z )
          getAngle(get the angle of bias)
'''

from smbus import SMBus
import math


class MPU6050(object):

    def __init__(self, port):
        self.MPU_ADDR = 0x68
        self.CONFIG = 0x1A
        self.GYRO_CONFIG = 0x1B
        self.SMPRT_DIV = 0x19
        self.ACCEL_CONFIG = 0x1c
        self.ACCEL_XOUT_H = 0x3B
        self.ACCEL_YOUT_H = 0x3D
        self.ACCEL_ZOUT_H = 0x3F
        self.GYRO_XOUT_H = 0x43
        self.GYRO_YOUT_H = 0x45
        self.GYRO_ZOUT_H = 0x47
        self.PWR_MGMT_1 = 0x6B
        self.INT_ENABLE = 0x38
        self.ob = SMBus(port)
        self.accelX = 0
        self.accelY = 0
        self.accelZ = 0
        self.gyroX = 0
        self.gyroY = 0
        self.gyroZ = 0
        self.angle = 0

    def init(self):
        self.ob.write_byte_data(self.MPU_ADDR, self.SMPRT_DIV, 0x07)
        self.ob.write_byte_data(self.MPU_ADDR, self.ACCEL_CONFIG, 0x00)
        # setting the range of acceleration to +/-2g
        self.ob.write_byte_data(self.MPU_ADDR, self.PWR_MGMT_1, 0x00)
        self.ob.write_byte_data(self.MPU_ADDR, self.CONFIG, 0x06)
        self.ob.write_byte_data(self.MPU_ADDR, self.GYRO_CONFIG, 0x00)
        # setting the range of angular velocity to +/- 250dec/s
        self.ob.write_byte_data(self.MPU_ADDR, self.INT_ENABLE, 0x01)

    def _read_word(self, addr):
        with self.ob as ob:

            high_num = ob.read_byte_data(self.MPU_ADDR, addr)
            low_num = ob.read_byte_data(self.MPU_ADDR, addr+1)
            value = (high_num << 8) | low_num  # get the 16bit'value

            if value >= 32768:
                value = value - 65536

            return value

    def _read_Xaccel(self):
        return self._read_word(self.ACCEL_XOUT_H)

    def _read_Yaccel(self):
        return self._read_word(self.ACCEL_YOUT_H)

    def _read_Zaccel(self):
        return self._read_word(self.ACCEL_ZOUT_H)

    def _read_Xgyro(self):
        return self._read_word(self.GYRO_XOUT_H)

    def _read_Ygyro(self):
        return self._read_word(self.GYRO_YOUT_H)

    def _read_Zgyro(self):
        return self._read_word(self.GYRO_ZOUT_H)

    def getAccel(self):
        self.accelX = self._read_Xaccel()/16384.0
        self.accelY = self._read_Yaccel()/16384.0
        self.accelZ = self._read_Zaccel()/16384.0
        return self.accelX, self.accelY, self.accelZ

    def getGyro(self):
        self.gyroX = self._read_Xgyro()/131.0
        self.gyroY = self._read_Ygyro()/131.0
        self.gyroZ = self._read_Zgyro()/131.0
        return self.gyroX, self.gyroY, self.gyroZ

    def getAngle(self):
        accelX, accelY, accelZ = self.getAccel()
        self.angle = math.atant(accelZ/accelY)
        return self.angle

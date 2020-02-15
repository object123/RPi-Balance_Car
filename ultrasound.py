'''
the class of ultrasound
author: object123
time 2020-2-4
function: getDist(get the distion)
          checkDist(judge the given value and system value)
          closeSound(reset the setting of IO of raspberryPi)
'''

import RPi.GPIO as GPIO
import time


class Ultrasound:

    def __init__(self, Echo, Trig):
        self.Echo = Echo
        self.Trig = Trig
        self.dist = 0

    def init(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.Echo, GPIO.IN)
        GPIO.setup(self.Trig, GPIO.OUT, initial=GPIO.LOW)

    def getDist(self):
        try:

            GPIO.output(self.Trig, GPIO.HIGH)
            time.sleep(0.000015)
            GPIO.output(self.Trig, GPIO.LOW)

            while not GPIO.input(self.Echo):
                pass
            t1 = time.time()
            while GPIO.input(self.Echo):
                pass
            t2 = time.time()
            self.dist = (t2 - t1)*34300/2
            return self.dist

        except KeyboardInterrupt:
            GPIO.cleanup()

    def checkDist(self, Adist):
        self.dist = self.getDist()

        if self.dist >= Adist:
            return True

        return False

    def closeSound():
        GPIO.cleanup()

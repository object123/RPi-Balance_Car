'''
author: object123
time: 2020-2-12
the encoder of motor
'''
import RPi.GPIO as GPIO
import time


class Encoder:

    def __init__(self, leftA, leftB, rightA, rightB):
        self.leftA = leftA
        self.leftB = leftB
        self.rightA = rightA
        self.rightB = rightB
        self.positionLeft = 0
        self.positionRight = 0

    def init(self):
        GPIO.setup([self.leftA, self.leftB], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup([self.rightA, self.rightB],
                   GPIO.IN,  pull_up_down=GPIO.PUD_UP)

    def _leftVelocityTest(self):
        if self.leftA == GPIO.LOW:
            if self.leftB == GPIO.LOW:
                self.positionLeft -= 1
            else:
                self.positionLeft += 1
        else:
            if self.leftB == GPIO.LOW:
                self.positionLeft += 1
            else:
                self.positionLeft -= 1

    def _rightVelocityTest(self):
        if self.rightA == GPIO.LOW:
            if self.rightB == GPIO.LOW:
                self.positionRight -= 1
            else:
                self.positionRight += 1
        else:
            if self.rightB == GPIO.LOW:
                self.positionRight += 1
            else:
                self.positionRight -= 1

    def start(self):
        GPIO.add_event_detect(self.leftA, GPIO.BOTH)
        GPIO.add_event_detect(self.leftB, GPIO.BOTH)
        GPIO.add_event_callback(self.leftA,
                                self._leftVelocityTest)
        GPIO.add_event_callback(self.leftB,
                                self._leftVelocityTest)
        GPIO.add_event_detect(self.rightB, GPIO.BOTH)
        GPIO.add_event_callback(
            self.rightB, self._rightVelocityTest)
        GPIO.add_event_detect(self.rightA, GPIO.BOTH)
        GPIO.add_event_callback(
            self.rightA, self._rightVelocityTest)

    def getPosition(self):
        return self.positionRight, self.positionLeft

    def close(self):
        GPIO.remove_event_detect(self.leftA)
        GPIO.remove_event_detect(self.leftB)
        GPIO.remove_evevt_detect(self.rightA)
        GPIO.remove_event_detect(GPIO.rightB)

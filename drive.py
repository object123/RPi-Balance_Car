'''
author: object123
time: 2020-2-11
the drive of wheel
'''
import RPi.GPIO as GPIO


class DRIVE:
    def __init__(self, left_in1, left_in2, pwmA, right_in1, right_in2, pwmB):
        self.left_in1 = left_in1
        self.left_in2 = left_in2
        self.pwmA = pwmA
        self.right_in1 = right_in1
        self.right_in2 = right_in2
        self.pwmB = pwmB

    def init(self, fruq):
        GPIO.setup([self.left_in1, self.left_in2, self.pwmA, self.right_in1,
                    self.right_in2, self.pwmB], GPIO.OUT)
        self.PWMA = GPIO.PWM(self.pwmA, fruq)
        self.PWMB = GPIO.PWM(self.pwmB, fruq)
        self.PWMA.start(0)
        self.PWMB.start(0)

    def goForward(self, pwm):
        GPIO.output([self.left_in1, self.right_in1], GPIO.HIGH)
        GPIO.output([self.Ain0, self.right_in2], GPIO.LOW)
        self.PWMA.ChangeDutyCycle(pwm)
        self.PWMB.ChangeDutyCycle(pwm)

    def goBack(self, pwm):
        GPIO.output([self.left_in1, self.right_in1], GPIO.LOW)
        GPIO.output([self.left_in2, self.right_in2], GPIO.HIGH)
        self.PWMA.ChangeDutyCycle(pwm)
        self.PWMB.ChangeDutyCycle(pwm)

    def goLeft(self, pwm):
        GPIO.output([self.left_in1, self.right_in2], GPIO.LOW)
        GPIO.output([self.left_in2, self.right_in1], GPIO.HIGH)

        self.PWMA.ChangeDutyCycle(pwm)
        self.PWMB.ChangeDutyCycle(pwm)

    def goRight(self, pwm):
        GPIO.output([self.left_in1, self.right_in2], GPIO.HIGH)
        GPIO.output([self.left_in2, self.right_in1], GPIO.LOW)

        self.PWMA.ChangeDutyCycle(pwm)
        self.PWMB.ChangeDutyCycle(pwm)

    def stop(self):
        GPIO.output([self.left_in1, self.right_in2], GPIO.LOW)
        GPIO.output([self.left_in2, self.right_in1], GPIO.LOW)

    def motor1Control(self, pwm):
        self.left_in1 = GPIO.HIGH
        self.left_in2 = GPIO.LOW
        self.PWMA.ChangeDutyCycle(pwm)

    def motor2Control(self, pwm):
        self.right_in1 = GPIO.HIGH
        self.right_in2 = GPIO.LOW
        self.PWMB.ChangeDutyCycle(pwm)

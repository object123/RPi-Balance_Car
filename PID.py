'''
author: object123
time: 2020-2-14
the pid algorithm
'''


class BalancePID:

    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.integral = 0
        self.

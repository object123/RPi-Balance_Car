'''
author: object123
time:2020-2-5

kalman filter algorithm
'''

import numpy as np


class Kalman_Filter:

    def __init__(self, Q_angle, Q_gyro, R_angle, dt):
        self.F = np.array([[1, -dt], [0, 1]])
        self.P = np.array([[1, 0], [0, 1]])
        self.Q = np.array([[Q_angle, 0], [0, Q_gyro]])
        self.B = np.array([[dt], [0]])
        self.H = np.array([1, 0])
        self.X = np.array([[0], [0]])
        self.R_angle = R_angle

    def kalmanRun(self, gyro, accelAngle):
        X_ = self.F.dot(self.X) + self.B*gyro
        P_temp = self.F.dot(self.P)
        P_ = P_temp.dot(self.F.T) + self.Q
        Kt = P_.dot(self.H.T)
        Division = self.P[0][0] + self.R_angle
        Kt = Kt/Division
        self.X = X_ + Kt*(accelAngle - X_[0][0])
        E = np.eye(2)
        self.P = (E - Kt.dot(self.H)).dot(P_)
        return self.X[0][0]


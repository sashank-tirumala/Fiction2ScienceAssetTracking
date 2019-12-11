from numpy import cos, sin
import numpy as np
def rotX(t):
    return np.array([[1,     0,       0],
                     [0,cos(t),-sin(t) ],
                     [0,sin(t), cos(t) ]])

def rotY(t):
    return np.array([[cos(t),   0,    sin(t)],
                     [0,        1,        0 ],
                     [-sin(t),  0,    cos(t)]])

def rotZ(t):
    return np.array([[cos(t), -sin(t), 0],
                     [sin(t),  cos(t), 0],
                     [0,            0, 1]])

def rotMatFromYPR(yaw, pitch, roll):
    return rotZ(yaw)@rotY(pitch)@rotX(roll)

def transformMatrix(x,y,z,yaw,pitch,roll):
    rotMat = rotMatFromYPR(yaw, pitch, roll)
    newMat = np.c_[rotMat, np.array([x,y,z])]
    newMat = np.vstack([newMat, np.array([0,0,0,1])])
    return newMat

x = 0.599542
y = -0.0573337
z = 0.0529168
yaw = -1.42216
pitch = 0.000161736
roll = 0.186929

calib_mat = np.linalg.inv(transformMatrix(x,y,z,yaw,pitch,roll))
np.save("calibration_matrix.npy",calib_mat)

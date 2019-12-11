import cv2
import numpy as np
from numpy import cos, sin

PI = np.pi
calib_mat = np.load("calibration_matrix.npy")
class RRect:
  def __init__(self, p0, s, ang):
    (self.W, self.H) = s
    self.ang = ang
    self.p0,self.p1,self.p2,self.p3 = self.get_verts(p0,s[0],s[1],ang)
    self.verts = [self.p0,self.p1,self.p2,self.p3]

  def get_verts(self, p0, W, H, ang):
    s = sin(ang)
    c = cos(ang)
    rotMat = np.array([[c,-s],[s,c]])
    v4 = np.array([p0[0], p0[1]]) + rotMat @ np.array([W/2, H/2])
    v1 = np.array([p0[0], p0[1]]) +  rotMat @ np.array([-W/2, H/2])
    v2 = np.array([p0[0], p0[1]]) + rotMat @ np.array([-W/2, -H/2])
    v3 = np.array([p0[0], p0[1]]) + rotMat @ np.array([W/2, -H/2])
    return [v1.astype(int),v2.astype(int),v3.astype(int),v4.astype(int)]

  def draw(self, image):
    # print(self.verts)
    for i in range(len(self.verts)-1):
      cv2.line(image, (self.verts[i][0], self.verts[i][1]), (self.verts[i+1][0],self.verts[i+1][1]), (0,255,0), 2)
    cv2.line(image, (self.verts[3][0], self.verts[3][1]), (self.verts[0][0], self.verts[0][1]), (0,255,0), 2)

def draw_rectangle(img, c1,c2):
	cv2.rectangle(img, c1,c2, (0,0,255),3 )

img = np.zeros((512, 512, 3), np.uint8) 
cv2.namedWindow('image') 

def parse_str(value):
    new_str = value.split(",")
    x = float(new_str[0])
    y = float(new_str[1])
    yaw = float(new_str[3])
    return(x,y,yaw)

def convert_to_pixel(x,y):
    newx = int(x*0.01)
    newy = int(y*0.01)
    pixelx = newx - 256
    pixely = newy - 256
"""
x right side is positive,
y downwards is positive,
z away is positive
"""
(W, H) = (30,60)
ang = PI/2 #degrees
P0 = (256,256)
while(1):
    f1 = open("example.txt")
    val = f1.readline()
    f1.close()
    x,y,yaw = parse_str(val)
    x,y = convert_to_pixel(x,y)
    rr = RRect((x,y),(W,H),yaw)
    rr.draw(img)
    cv2.imshow('image', img)
    # draw_rectangle(img, (0,0), (512,512))
    k = cv2.waitKey(1)
    if(k == ord('q')):
        break
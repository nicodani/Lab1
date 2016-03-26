#! /usr/bin/python
from SimpleCV import Camera, Display, Image
cam=Camera()
img=cam.getImage()
img.save("foto1.jpg")



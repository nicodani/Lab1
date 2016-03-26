#! /usr/bin/python
from SimpleCV import Camera, Display, Image
import time
c=Camera()
img=c.getImage()
img.save("Original.jpg")
fot=img.show()
time.sleep(4)
fot.quit()
img2=img.grayscale()
fot2=img2.show()
img2.save("EscalaGrises.jpg")
time.sleep(4)
fot2.quit()

















































































import os
import time
import picamera

usb = "/media/usb-drive/"
file = "img{counter:08d}.jpg"


with picamera.PiCamera() as camera:
    camera.resolution = (2464,2464)
    time.sleep(2)
    for filename in camera.capture_continuous(file, format = "jpeg", quality = 100):
        print('Captured %s' % filename)
        time.sleep(1)

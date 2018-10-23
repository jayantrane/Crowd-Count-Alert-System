import cv2
import time
import test

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self,count):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        etcount=0
        side = 'o'
        if(count%20==0):
            count/=100
            cv2.imwrite( "../data/test/images/IMG_" + "1.jpg", image)
            etcount, side = test.testimage('B', 0)
        else:
            time.sleep(0.05)
        return (jpeg.tobytes(),etcount, side)
    
    
class VideoCamera2(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture('../data/vid3.mp4')
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self,count):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        etcount=0
        side = 'o'
        if(count%20==0):
            count/=100
            cv2.imwrite( "../data/test/images2/IMG_" + "1.jpg", image)
            etcount, side = test.testimage('A', 1)
        else:
            time.sleep(0.05)
        return (jpeg.tobytes(),etcount, side)

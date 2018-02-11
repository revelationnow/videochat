#/env/python3
import numpy as np
import cv2

class Video:
    def __init__(self):
        self._capture = None

    def startVideo(self):
        self._capture = cv2.VideoCapture(0)

    def getFrame(self):
        ret, frame = self._capture.read()
        return frame

    def stopVideo(self):
        self._capture.release()









#/env/python3

import numpy as np
import cv2
from video import Video

test = Video()

test.startVideo()

while(True):
    frame = test.getFrame()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()



#!/usr/bin/env python3

import numpy as np
import cv2
from video import Video
from socket import AsyncSocketClient
from socket import AsyncSocketServer

video_obj = Video()
socket_serv = AsyncSocketServer()
socket_client = AsyncSocketClient()

socket_serv.start_socket('127.0.0.1',23456)
# STATE : MEANING
#     0 : DISCONNECTED
#     1 : CONNECTED
conn_state = 0

while True:
    data = socket_serv.get_data()
    if data[0] = True:
        conn_state = 1
        cv2.imshow('frame',data[1])



video_obj.startVideo()

while True :
    frame = video_obj.getFrame()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()


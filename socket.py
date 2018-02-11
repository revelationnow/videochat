#/usr/bin/env python3
import numpy as np
import socket
import sys
import asyncore

class AsyncSocketServer(asyncore.dispatcher):
    def __init__(self):
        self._socket = None
        self._data = None
        self._new_data = False
        asyncore.dispatcher.__init__(self)

    def start_socket(self, address, port):
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((address, port))
        self.listen(5)
        print("Listening to ", address," on port",port)

    def handle_accept(self):
        pair = self.accept()
        self._data = None
        if pair is not None:
            sock, addr = pair
            print("Received data from ",addr)
            self._data = sock.recv(1000000)
            self._new_data = True


    def get_data(self):
        self._new_data = False
        return self._data


class AsyncSocketClient(asyncore.dispatcher):
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self._socket = None
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self._buffer = ""
        self._recd_data = None
        self._new_recd_data = False

    def connect(self, addr, port):
        self._dest_addr = addr
        self._dest_port = port
        self.connect((addr, port))

    def writeable(self):
        return (len(self._buffer) > 0)

    def handle_write(self):
        sent = self.send(self._buffer)
        self._buffer = self._buffer[sent:]

    def handle_read(self):
        self._new_recd_data = True
        self._recd_data = self.recv(1000000)

    def get_data(self):
        self._new_recd_data = False
        return self._recd_data


    def write(self, data):
        self._buffer = data

    def handle_close(self):
        self.close()







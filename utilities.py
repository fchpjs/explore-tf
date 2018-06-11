import cv2
from threading import Thread
from time import sleep


class VideoStream:
    def __init__(self, src=0, emulation=True):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.fps = self.stream.get(cv2.CAP_PROP_FPS)
        self.height = self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.width = self.stream.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.counter = 0
        self.emulation = emulation

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            (self.grabbed, self.frame) = self.stream.read()
            self.counter += 1
            if self.fps > 0 and self.emulation:
                sleep(1000 / self.fps / 1000)

    def read(self):
        return self.frame, self.counter

    def stop(self):
        self.stopped = True
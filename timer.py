import time


class timer:
    def __init__(self):
        self.__start = 0

    def startTimer(self):
        self.__start = time.time()

    def timeCheck(self):
        if self.__start != 0:
            duration = time.time() - self.__start
            stringOut = str(round(duration, 2)) + " sec elapsed"
            return stringOut
        else:
            print("timer not started")

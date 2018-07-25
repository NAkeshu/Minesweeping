"""
想做一个计时器，每秒都update一下messageText，
但是好像需要用到多线程（？）
不太会，先保留这个功能
"""
import time

class Timer():
    def __init__(self):
        self.startTime = int(time.time())
        print(str(self.startTime))

    def timing(self, timeMessage):
        curtime = int(time.time())
        usedTime = curtime - self.startTime
        timeMessage["text"] += str(usedTime)
        timeMessage.update()


if __name__ == "__main__":
    Timer()
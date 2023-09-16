from Counters import *

class Lap:
    #this is a lap class to add into the StopwatchController class


    def __init__(self):
        self.lap = 0
        self._timekeeper = TimeKeeper() 
        #adding timekeeper here seemed to do the trick
        #before adding time keeper it would not show a number


    def add(self):
        self.lap += 1
        self._timekeeper.start()


    def reset(self):
        self.lap = 0

    def current(self):
        return self.lap

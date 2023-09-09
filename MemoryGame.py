import time
from Button import *
from Displays import *
from Lights import *
from Buzzer import *
from Counters import *

class MemoryGame:
    """
    this is the class for the memory game that 
    will include a sequence of lights the player
    must mimic based on buttons and a display screen
    that shows player level and a buzzer that 
    announces a win

    I am thinking this class will call on the other 
    two classes, not too sure if i am doing this
    right
    """

    def __init__(self):
     self._number = 0
     self.display()


class Score:
    """
    This class keeps track of the player score
    """

    def __init__(self):
     self._winBuz = Buzzer(15)
     self._lossBuz = Buzzer(15)
     self._gameLevel = Counter(0)
     self._display = LCDDisplay(sda = 0, scl = 1, i2cid = 0)

    
    def run(self):
        """ Keeps app running so """
        while True:
            time.sleep(0.5)

    def display(self):
        """ show the welcome message on the display """
    
        self._display.showText("Lets Play")
        


    def displayResult(self)
    """
    if buttonSequence is true
    print "level up"
    if buttonSequence is false
    print "better luck next time"
    """

    def trumpet(self)
    """
    if buttonSequence is true
    winBuz
    if buttonSequence is false
    lossBuz
    """

    def levelUp(self)
    """
    if buttonSequence is true
    increase gameLevel
    """

    def reset(self)
    """
    if buttonSequence is false
    reset counter
    """




class PlayGame:
    """
    This class is for random light sequence and
    buttons matching up to the order of each light
    """

    def __init__(self):
     self._redbutton = Button(28, "red", buttonhandler=self)
     self._yellowbutton = Button(16, "yellow", buttonhandler=self)
     self._greenbutton = Button(26, "green", buttonhandler=self)
     self._redlight = Light(3, "red led")
     self._yellowlight = Light(14, "yellow led")
     self._greenlight = Light(10, "green led")

    def lightSequence(self)
    """
    lihts blink in a random sequence
    """

    def buttonsPressed(self)
    """
    buttons pressed in the same sequence as lights
    """

    def buttonSequence(self)
    """
    checks to see if buttons were pressed
    in the correct sequence in true or false
    statement
    """
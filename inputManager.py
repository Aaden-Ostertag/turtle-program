import tkinter
from constants import *

buttons = {
    0: False, # left mouse
    1: False # right mouse
}

buttonID = 0

def onPress(buttonID, action):
    buttonID = buttonID - 1
    if not buttons[buttonID]:
        buttons[buttonID] = True
        action()


def onRelease(buttonID):
    buttonID = buttonID - 1
    if buttons[buttonID]:
        buttons[buttonID] = False
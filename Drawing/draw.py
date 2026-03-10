from constants import *
import inputManager as im

def draw(x, y, buttonID):
    im.onPress(buttonID, draw(x, y))

def draw(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

    t.dot()
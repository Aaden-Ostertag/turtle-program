import turtle
import tkinter as tk
import math
import random as r
from ..constants import *
from utils import *

def draw_circle(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    
    screen.colormode(255)
    t.pencolor()

    radius = 50
    diameter = radius * 2
    circumference = 2 * math.pi * radius

    for _ in range(360):
        t.forward(circumference/360)
        t.left(1)
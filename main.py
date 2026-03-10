import turtle 
import tkinter as tk
from utils import *
from constants import *
from Drawing.draw import draw
import inputManager as im

def main():
    t.onclick(lambda x, y: draw(x, y, 1), 1) # left mouse button state

if __name__ == "__main__":
    main()

screen.mainloop()
from window import Window
from maze import Maze

win = Window(800, 600)
g = Game(10, 10, 15, 15, 20, 20, win)
win.wait_for_close()
from window import Window
from game import Difficulty, Game

win = Window(500, 500)
g = Game(Difficulty.BEGINNER, win)
win.wait_for_close()
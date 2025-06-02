from window import Window
from game import Game

win = Window()
difficulty = win.choose_difficulty()
g = Game(difficulty, win)
win.wait_for_close()
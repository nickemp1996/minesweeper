import time
import random
from cell import Cell
from enum import Enum

Difficulty = Enum('Difficulty', ['BEGINNER', 'INTERMEDIATE', 'EXPERT'])

class Game:
	def __init__(self, difficulty, win, seed=None):
	    self._difficulty = difficulty
	    self._win = win
	    if seed:
	    	random.seed(seed)
	    if self._difficulty == Difficulty.BEGINNER:
	    	self.num_rows = 9
	    	self.num_cols = 9
	    	self.num_mines = 10
	    elif self._difficulty == Difficulty.INTERMEDIATE:
	    	self.num_rows = 16
	    	self.num_cols = 16
	    	self.num_mines = 40
	    elif self._difficulty == Difficulty.EXPERT:
	    	self.num_rows = 30
	    	self.num_cols = 16
	    	self.num_mines = 99
	    else:
	    	raise Exception(f"Invalid Difficulty level: {self._difficulty}")
	    self._create_cells()

	def _create_cells(self):
	    self._cells = []
	    for i in range(self.num_rows):
	        row = []
	        for j in range(self.num_cols):
	            cell = Cell(2, 2)
	            row.append(cell)
	        self._cells.append(row)
	        
	    # Now that all cells exist in the structure, draw them
	    for i in range(self.num_rows):
	        for j in range(self.num_cols):
	            self._cells[i][j]._create_button(i, j, self._win)
	            self._animate()

	def _animate(self):
		self._win.redraw()
		time.sleep(0.05)

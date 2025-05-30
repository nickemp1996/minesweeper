import time
import random
from cell import Cell

class Game:
	def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
	    self.x1 = x1
	    self.y1 = y1
	    self.num_rows = num_rows
	    self.num_cols = num_cols
	    self.cell_size_x = cell_size_x
	    self.cell_size_y = cell_size_y
	    self._win = win
	    if seed:
	    	random.seed(seed)
	    self._create_cells()

	def _create_cells(self):
	    self._cells = []
	    for i in range(self.num_rows):
	        row = []
	        for j in range(self.num_cols):
	            cell = Cell(self._win)
	            row.append(cell)
	        self._cells.append(row)
	        
	    # Now that all cells exist in the structure, draw them
	    for i in range(self.num_rows):
	        for j in range(self.num_cols):
	            self._cells[i][j]._create_button(i, j)

	def _animate(self):
		self._win.redraw()
		time.sleep(0.05)

import time
import random
from cell import Cell
from my_enums import Difficulty

class Game:
	def __init__(self, difficulty, win, seed=None):
	    self._difficulty = difficulty
	    self._win = win
	    self.num_cells_open = 0
	    self.num_cells_flagged = 0
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
	    	self.num_rows = 16
	    	self.num_cols = 30
	    	self.num_mines = 99
	    else:
	    	raise Exception(f"Invalid Difficulty level: {self._difficulty}")
	    self._identify_mines()
	    self._create_cells()

	def _identify_mines(self):
		self.mines = set()
		while len(self.mines) < self.num_mines:
			row = random.randint(0, self.num_rows - 1)
			column = random.randint(0, self.num_cols - 1)
			mine_coordinates = (row, column)
			self.mines.add(mine_coordinates)
		print(self.mines)

	def _create_cells(self):
	    self._cells = []
	    for i in range(self.num_rows):
	        row = []
	        for j in range(self.num_cols):
	            is_mine = (i, j) in self.mines
	            cell = Cell(25, 25, is_mine, self)
	            row.append(cell)
	        self._cells.append(row)
	        
	    # Now that all cells exist in the structure, create buttons and discover neighbors that are mines
	    for i in range(self.num_rows):
	        for j in range(self.num_cols):
	        	self._cells[i][j]._create_button(i, j, self._win)
	        	self._identify_neighboring_mines(self._cells[i][j])

	def _identify_neighboring_mines(self, cell):
		if cell._is_mine:
			#this cell is a mine, no need to count neighboring mines
			return
		neighbors = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
		#Top row edge cases
		if cell._row == 0:
			if cell._col == 0:
				#cell is at the top left
				#valid neighbors: east, southeast, south
				my_neighbors = neighbors[2:5]
			elif cell._col == self.num_cols - 1:
				#cell is at the top right
				#valid neighbors: south, southwest, west
				my_neighbors = neighbors[4:7]
			else:
				#cell between top-left and top-right
				#valid neighbors: east, southeast, south, southwest, west
				my_neighbors = neighbors[2:7]
		#Bottom row edge cases
		elif cell._row == self.num_rows - 1:
			if cell._col == 0:
				#cell is at the bottom left
				#valid neighbors: north, northeast, east
				my_neighbors = neighbors[0:3]
			elif cell._col == self.num_cols - 1:
				#cell is at the bottom right
				#valid neighbors: north, west, northwest
				my_neighbors = [neighbors[0]] + neighbors[6:]
			else:
				#cell is between bottom-left and bottom-right
				#valid neighbors: north, northeast, east, west, northwest
				my_neighbors = neighbors[0:3] + neighbors[6:]
		#Left column edge cases
		elif cell._col == 0:
			#already handled top-left and bottom-left
			if cell._row > 0 and cell._row < self.num_rows - 1:
				#cell is between the top-left and bottom-left
				#valid neighbors: north, northeast, east, southeast, south
				my_neighbors = neighbors[0:5]
		#Right column edge cases
		elif cell._col == self.num_cols - 1:
			#already handled top-right and bottom-right
			if cell._row > 0 and cell._row < self.num_rows - 1:
				#cell is between top-right and bottom-right
				#valid neighbors: north, south, southwest, west, northwest
				my_neighbors = [neighbors[0]] + neighbors[4:]
		#all edge cases handled, remaining cells are inner cells with 8 neighbors
		else:
			my_neighbors = neighbors

		for neighbor in my_neighbors:
			i = cell._row + neighbor[0]
			j = cell._col + neighbor[1]
			cell._neighbors.append(self._cells[i][j])
			if self._cells[i][j]._is_mine:
				cell._num_neighboring_mines += 1

	def _uncover_mines(self):
		for mine in self.mines:
			i = mine[0]
			j = mine[1]
			self._cells[i][j]._non_event_open()

	def you_lost_haha(self):
		try_again = self._win.restart_or_quit()
		if try_again:
			difficulty = self._win.choose_difficulty()
			self.change_difficulty(difficulty)
			self._identify_mines()
			self._create_cells()
		else:
			self._win.close()

	def check_for_win(self):
		if self.num_cells_open == (self.num_rows * self.num_cols) - self.num_mines:
			self.you_won()

	def you_won(self):
		self._win.open_gif('images/you-win-winner.gif')
		try_again = self._win.restart_or_quit()
		if try_again:
			difficulty = self._win.choose_difficulty()
			self.change_difficulty(difficulty)
			self._identify_mines()
			self._create_cells()
		else:
			self._win.close()

	def change_difficulty(self, difficulty):
		self.num_cells_open = 0
		self.num_cells_flagged = 0
		self._difficulty = difficulty
		if self._difficulty == Difficulty.BEGINNER:
			self.num_rows = 9
			self.num_cols = 9
			self.num_mines = 10
		elif self._difficulty == Difficulty.INTERMEDIATE:
			self.num_rows = 16
			self.num_cols = 16
			self.num_mines = 40
		elif self._difficulty == Difficulty.EXPERT:
			self.num_rows = 16
			self.num_cols = 30
			self.num_mines = 99
		else:
			raise Exception(f"Invalid Difficulty level: {self._difficulty}")


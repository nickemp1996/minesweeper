import tkinter as tk

class Cell:
	def __init__(self, width, height, is_mine, is_rick_roll, game):
		self.i = tk.PhotoImage(width=1, height=1)
		self.flag = tk.PhotoImage(file='images/Minesweeper_Flag.png')
		self.mine = tk.PhotoImage(file='images/Minesweeper_Mine.png')
		self._is_mine = is_mine
		self._flagged = False
		self._is_rick_roll = is_rick_roll
		self._num_neighboring_mines = 0
		self._neighbors = []
		self._width = width
		self._height = height
		self._button = None
		self._game = game
		self._colors = ["white", "blue", "green", "red", "purple4", "maroon", "cyan", "purple", "gray"]

	def _create_button(self, row, col, win):
		self._row = row
		self._col = col
		self._button = tk.Button(win._frame2,
								image = self.i,
								compound = 'c',
								width = self._width,
								height = self._height,
								)
		self._button.grid(row = self._row, column = self._col)
		self._button.bind("<Button-1>", self._open)
		self._button.bind("<Button-3>", self._flag)

	def _open(self, event):
		if self._game.num_cells_open == 0 and self._game.num_cells_flagged == 0:
			self._game.start_timer()
		if self._button['state'] == tk.NORMAL and not self._flagged:
			self._button['state'] = tk.DISABLED
			if self._is_mine:
				self._button.config(image=self.mine)
				self._game._uncover_mines()
				self._game.you_lost_haha()
			elif self._is_rick_roll:
				self._game.rick_roll()
			else:
				self._game.num_cells_open += 1
				if self._flagged:
					self._button.config(image="")
					self._flagged = False
					self._game.num_cells_flagged -= 1
				if self._num_neighboring_mines > 0:
					color = self._colors[self._num_neighboring_mines]
					self._button.config(text=f"{self._num_neighboring_mines}")
					self._button.config(highlightbackground=color)
				else:
					self._open_neighbors()
			self._game.check_for_win()

	def _non_event_open(self):
		if self._button['state'] == tk.NORMAL:
			if self._is_mine and not self._flagged:
				self._button.config(image=self.mine)
				self._button['state'] = tk.DISABLED

	def _flag(self, event):
		if self._game.num_cells_open == 0 and self._game.num_cells_flagged == 0:
			self._game.start_timer()
		if self._button['state'] == tk.NORMAL:
			if self._flagged:
				self._button.config(image=self.i)
				self._flagged = False
				self._game.num_cells_flagged -= 1
				self._game.update_flags()
			else:
				if self._game.num_cells_flagged < self._game.num_mines:
					self._button.config(image=self.flag)
					self._flagged = True
					self._game.num_cells_flagged += 1
					self._game.update_flags()

	def _open_neighbors(self):
		for neighbor in self._neighbors:
			self._open_neighbors_r(neighbor)

	def _open_neighbors_r(self, neighbor):
		if neighbor._is_mine:
			return
		if neighbor._flagged:
			return
		if neighbor._button['state'] == tk.DISABLED:
			return
		else:
			self._game.num_cells_open += 1
			if neighbor._num_neighboring_mines > 0:
				color = neighbor._colors[neighbor._num_neighboring_mines]
				neighbor._button.config(relief=tk.SUNKEN)
				neighbor._button.config(text=f"{neighbor._num_neighboring_mines}")
				neighbor._button.config(highlightbackground=color)
				neighbor._button['state'] = tk.DISABLED
				return
			else:
				neighbor._button.config(relief=tk.SUNKEN)
				neighbor._button['state'] = tk.DISABLED
				for neighbors_neighbor in neighbor._neighbors:
					neighbor._open_neighbors_r(neighbors_neighbor)

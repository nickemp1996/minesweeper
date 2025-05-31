import tkinter as tk

class Cell:
	def __init__(self, width, height, is_mine):
		self.flag = tk.PhotoImage(file='images/Minesweeper_Flag.png')
		self.mine = tk.PhotoImage(file='images/Minesweeper_Mine.png')
		self._is_mine = is_mine
		self._flagged = False
		self._num_neighboring_mines = 0
		self._neighbors = []
		self._text = ""
		self._width = width
		self._height = height
		self._button = None

	def _create_button(self, row, col, win):
		self._row = row
		self._col = col
		self._button = tk.Button(win._root, 
								text = self._text,
								width = self._width,
								height = self._height,
								)
		self._button.grid(row = self._row, column = self._col)
		self._button.bind("<Button-1>", self._open)
		self._button.bind("<Button-3>", self._flag)

	def _open(self, event):
		if self._button['state'] == tk.NORMAL:
			if self._is_mine:
				self._button.config(image=self.mine)
				print("GAME OVER")
			else:
				if self._flagged:
					self._button.config(image="")
					self._button.image = None
					self._flagged = False
				if self._num_neighboring_mines > 0:
					self._button.config(text=f"{self._num_neighboring_mines}")
				else:
					self._open_neighbors()
			self._button['state'] = tk.DISABLED

	def _flag(self, event):
		if self._button['state'] == tk.NORMAL:
			if self._flagged:
				self._button.config(image="")
				self._button.image = None
				self._flagged = False
			else:
				self._button.config(image=self.flag)
				self._flagged = True

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
			if neighbor._num_neighboring_mines > 0:
				neighbor._button.config(relief=tk.SUNKEN)
				neighbor._button.config(text=f"{neighbor._num_neighboring_mines}")
				neighbor._button['state'] = tk.DISABLED
				return
			else:
				neighbor._button.config(relief=tk.SUNKEN)
				neighbor._button['state'] = tk.DISABLED
				for neighbors_neighbor in neighbor._neighbors:
					neighbor._open_neighbors_r(neighbors_neighbor)

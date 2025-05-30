import tkinter as tk

class Cell:
	def __init__(self, width, height, row, column, win):
		self._is_mine = False
		self._flagged = False
		self._opened = False
		self._num_neighboring_mines = 0
		self._text = ""
		self._width = width
		self._height = height
		self._win = win
		self._button = None

	def _create_button(self, row, col):
		self._button = tk.Button(self._win.__root, 
								text = self._text,
								width = self._width,
								height = self._height,
								)
		self._button.grid(row = row, column = col)
		self._button.bind("<Button-1>", self._open)
		self._button.bind("<Button-3>", self._flag)

	def _open(self, event):
		if self.opened:
			return

	def _flag(self):
		pass
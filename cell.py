import tkinter as tk

class Cell:
	def __init__(self, width, height, is_mine):
		self.flag = tk.PhotoImage(file='images/Minesweeper_Flag.png')
		self.mine = tk.PhotoImage(file='images/Minesweeper_Mine.png')
		self._is_mine = is_mine
		self._flagged = False
		self._num_neighboring_mines = 0
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
				if self._num_neighboring_mines > 0:
					self._button.config(text=f"{self._num_neighboring_mines}")
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
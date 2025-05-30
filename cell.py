import tkinter as tk
import pathlib, os

flag = "images/Minesweeper_Flag.png"
current_dir = pathlib.Path(__file__).parent.resolve()
img_path = os.path.join(current_dir, flag)

class Cell:
	def __init__(self, width, height):
		self.flag = tk.PhotoImage(file='images/Minesweeper_Flag.png')
		self._is_mine = False
		self._flagged = False
		self._num_neighboring_mines = 0
		self._text = ""
		self._width = width
		self._height = height
		self._button = None

	def _create_button(self, row, col, win):
		self._button = tk.Button(win._root, 
								text = self._text,
								width = self._width,
								height = self._height,
								)
		self._button.grid(row = row, column = col)
		self._button.bind("<Button-1>", self._open)
		self._button.bind("<Button-3>", self._flag)

	def _open(self, event):
		if self._button['state'] == tk.NORMAL:
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
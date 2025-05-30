from tkinter import Tk, BOTH, Canvas

class Window:
	def __init__(self, width, height):
		self._root = Tk()
		self._root.title = "Minesweeper"
		self._root.protocol("WM_DELETE_WINDOW", self.close)
		self._running = False

	def redraw(self):
		self._root.update_idletasks()
		self._root.update()

	def wait_for_close(self):
		self._running = True
		while self._running:
			self.redraw()

	def close(self):
		self._running = False

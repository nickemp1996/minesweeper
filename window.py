from tkinter import Tk, Toplevel, Button
from my_enums import Difficulty

class Window:
	def __init__(self):
		self._root = Tk()
		self._root.title("Minesweeper")
		self._root.protocol("WM_DELETE_WINDOW", self.close)
		self._running = False

	def choose_difficulty(self):
	    popup = Toplevel(self._root)
	    popup.title("Choose Difficulty")
	    result = None

	    def set_result(value):
	        nonlocal result
	        result = value
	        popup.destroy()

	    button_1 = Button(popup, text="Beginner", command=lambda: set_result(Difficulty.BEGINNER))
	    button_1.pack(pady=10)
	    button_2 = Button(popup, text="Intermediate", command=lambda: set_result(Difficulty.INTERMEDIATE))
	    button_2.pack(pady=10)
	    button_3 = Button(popup, text="Expert", command=lambda: set_result(Difficulty.EXPERT))
	    button_3.pack(pady=10)

	    popup.wait_window()
	    button_1.destroy()
	    button_2.destroy()
	    button_3.destroy()
	    return result

	def restart_or_quit(self):
	    popup = Toplevel(self._root)
	    popup.title("Try Again?")
	    result = None

	    def set_result(value):
	        nonlocal result
	        result = value
	        popup.destroy()

	    button_1 = Button(popup, text="Try Again?", command=lambda: set_result(True))
	    button_1.pack(pady=10)
	    button_2 = Button(popup, text="Quit", command=lambda: set_result(False))
	    button_2.pack(pady=10)

	    popup.wait_window()
	    button_1.destroy()
	    button_2.destroy()
	    return result

	def redraw(self):
		self._root.update_idletasks()
		self._root.update()

	def wait_for_close(self):
		self._running = True
		while self._running:
			self.redraw()

	def close(self):
		self._running = False

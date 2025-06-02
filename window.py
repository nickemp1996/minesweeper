import time
from tkinter import Tk, Toplevel, Button, Label
from PIL import Image, ImageTk
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
	    popup.title("Play Again?")
	    result = None

	    def set_result(value):
	        nonlocal result
	        result = value
	        popup.destroy()

	    button_1 = Button(popup, text="Play Again?", command=lambda: set_result(True))
	    button_1.pack(pady=10)
	    button_2 = Button(popup, text="Quit", command=lambda: set_result(False))
	    button_2.pack(pady=10)

	    popup.wait_window()
	    button_1.destroy()
	    button_2.destroy()
	    return result

	def play_gif(self, frames, delay):
	    popup = Toplevel(self._root)
	    label = Label(popup)
	    label.pack()
	    def update(index):
	        if index >= len(frames):
	            index = 0
	        label.config(image=frames[index])
	        label.after(delay, update, index + 1)
	    update(0)
	    result = None

	    def set_result(value):
	        nonlocal result
	        result = value
	        popup.destroy()

	    button_1 = Button(popup, text="Play Again?", command=lambda: set_result(True))
	    button_1.pack(pady=10)
	    button_2 = Button(popup, text="Quit", command=lambda: set_result(False))
	    button_2.pack(pady=10)

	    popup.wait_window()
	    button_1.destroy()
	    button_2.destroy()
	    return result

	def open_gif(self, file_path):
	    try:
	        gif = Image.open(file_path)
	        frames = []
	        try:
	            for i in range(gif.n_frames):
	                gif.seek(i)
	                frame = gif.copy()
	                frame = ImageTk.PhotoImage(frame)
	                frames.append(frame)
	        except EOFError:
	            pass
	        delay = gif.info.get("duration", 100)
	        return self.play_gif(frames, delay)
	    except Exception as e:
	        print(f"Error loading GIF: {e}")

	def redraw(self):
		self._root.update_idletasks()
		self._root.update()

	def wait_for_close(self):
		self._running = True
		while self._running:
			self.redraw()

	def close(self):
		self._running = False

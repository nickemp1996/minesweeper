import tkinter.font as tkFont
from tkinter import Tk, Toplevel, Button, Label, Frame
from PIL import Image, ImageTk
from my_enums import Difficulty

class Window:
	def __init__(self):
		self._root = Tk()
		self._root.title("Minesweeper")
		self._root.protocol("WM_DELETE_WINDOW", self.close)
		self._frame1 = Frame(self._root, width=200, height=100)
		self._frame1.pack()
		self._frame2 = Frame(self._root)
		self._frame2.pack()
		self._running = False
		self._digital_font = tkFont.Font(family="digital_font", size=36)
		self.seconds = 0
		self.rollover = 0
		self.timer_running = False
		self._create_indicators()

	def _create_indicators(self):
		self._frame1_label_flags = Label(self._frame1, text="000", font=self._digital_font, bg="black", fg="red")
		self._frame1_label_flags.pack(padx=25, side="left")
		self._frame1_label_timer = Label(self._frame1, text="000", font=self._digital_font, bg="black", fg="red")
		self._frame1_label_timer.pack(padx=25, side="right")

	def update_flags(self, flags_left):
		if flags_left < 10:
			self._frame1_label_flags.config(text=f"00{flags_left}")
		else:
			self._frame1_label_flags.config(text=f"0{flags_left}")

	def update_timer(self):
		if self.timer_running:
			self.seconds += 1
			if self.seconds < 10:
				self._frame1_label_timer.config(text=f"00{self.seconds}")
			elif self.seconds >=10 and self.seconds < 100:
				self._frame1_label_timer.config(text=f"0{self.seconds}")
			elif self.seconds >=100 and self.seconds < 1000:
				self._frame1_label_timer.config(text=f"{self.seconds}")
			else:
				self.seconds = 0
				self.rollover += 1
				self._frame1_label_timer.config(text=f"00{self.seconds}")
			self._root.after(1000, self.update_timer)

	def stop_timer(self):
		self.timer_running = False

	def reset_timer(self):
		self.seconds = 0
		self.rollover = 0
		self._frame1_label_timer.config(text=f"00{self.seconds}")

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

	def play_gif(self, frames, delay, title):
	    popup = Toplevel(self._root)
	    popup.title(title)
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

	def open_gif(self, file_path, title):
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
	        return self.play_gif(frames, delay, title)
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

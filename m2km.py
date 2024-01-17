import tkinter as tk

WIDTH:int = 360
HEIGHT:int = 240

TITLE = "Miles 2 Kilometers"

window = tk.Tk()

window.title(TITLE)
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable = False


window.mainloop()
# Widget mantojums un izkartojums

# https://docs.python.org/3/library/tkinter.html
import tkinter as tk
from tkinter import ttk # Modernāks izskāts priekš GUI Widgets


# 1. Izveidot programmas logu
logs = tk.Tk() # logs (window) - Galvenais el.
logs.title("Tkinter Frame el.") # loga nosaukums
logs.geometry("600x400") # loga izmērs "PlatumsxAugstums"


# 2. Aizpildīšana ar elementiem
frame = ttk.Frame(master=logs, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
# frame.pack_propagate(False)
# frame.pack(side="left") # side - izkartojums uz loga
frame.pack()

text = ttk.Label(master=frame, text="Label iekšā Frame")
text.pack(side="left")

button = ttk.Button(master=frame, text="Button iekšā Frame")
button.pack(side="left", padx=10)

# 3. Palaist
logs.mainloop() 

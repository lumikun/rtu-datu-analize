import tkinter as tk
from tkinter import ttk

# Logs
logs = tk.Tk()
logs.title("Grid - reste")
logs.geometry("600x400")

# Widgets
label1 = ttk.Label(logs, text="1.", background="blue")
label2 = ttk.Label(logs, text="Šīs ir Label 2", background="green")
label3 = ttk.Label(logs, text="Label 3 ar garāku tekstu", background="red")
button1 = ttk.Button(logs, text="Button 1")
button2 = ttk.Button(logs, text="Button 2")

# Grid (restes) definēšana
logs.columnconfigure((0,1,2), weight=1, uniform="a")
# logs.columnconfigure(2, weight=3, uniform="a")
logs.rowconfigure(0, weight=1, uniform="a")
logs.rowconfigure(1, weight=1, uniform="a")
logs.rowconfigure(2, weight=1, uniform="a")
logs.rowconfigure(3, weight=2, uniform="a")

# Widget izkartojums
label1.grid(row=0, column=0, columnspan=3, sticky="nsew")
label2.grid(row=2, column=2, sticky="nsew")
label3.grid(row=1, column=1, rowspan=2, sticky="nsew", padx=15)
button1.grid(row=3, column=0)
button2.grid(row=3, column=2)


# Palaišana
logs.mainloop()
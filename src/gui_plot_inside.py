import tkinter as tk
from tkinter import ttk
from tkinter import filedialog # Failu atvēršanai
from matplotlib.figure import Figure # grafiks zīmēšanai kaut kur (citā programmā)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # grafika zīmēšana tkinterā
import pandas as pd
from random import randint

data: pd.DataFrame = None

def update_plot():
    global data
    plot.clear()
    if type(data) == pd.DataFrame: # data nav tukšs
        x = data.columns[0]
        y = data.columns[1]
        print(f"{data[x]}\n{data[y]}")
        plot.plot(data[x], data[y])
    else:
        quantity = randint(7,15)
        x = [n for n in range(1, quantity+1)] # list comprehension
        # x = []
        # for n in range(1, randint(5,10)+1):
        #     if n % 2:
        #         x.append(n)
        y = [randint(10, 100) for _ in range(1, quantity+1)]
        plot.plot(x, y)
    canvas.draw()

def load_file():
    file_path = filedialog.askopenfilename() # nevajag pathlib
    if file_path:
        global data
        data = pd.read_csv(file_path)
        print(data)



# Loga veidošana
window = tk.Tk()
window.title("Matplotlib inside Tkinter")

button_load = ttk.Button(window, text="Atvērt CVS", command=load_file)
button_load.pack(padx=10, pady=10)

button = ttk.Button(window, text="Uzzīmēt grafiku", command=update_plot)
button.pack(padx=10, pady=10)

# Vienkaršs matplotlib grafiks
fig = Figure(figsize=(6, 4), dpi=100) # 600x400 px
plot = fig.add_subplot(111) # 1 rinda, 1 kolonna, 1 index
plot.plot([1,2,3,4,5,6,7], [10, 20, 25, 40, 50, 75, 90])
# plt.show() # lai zīmētu bez papildus grafiskas vides

# Piesaistām grafika pie Tkinter loga
canvas = FigureCanvasTkAgg(figure=fig, master=window)
canvas.draw()

# Zīmējam grafiku uz Tkinter
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Tkinter darba cikls
window.mainloop()
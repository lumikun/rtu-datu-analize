import pandas
import matplotlib.pyplot as plt
import seaborn as sns

import tkinter as tk
from tkinter import ttk
from pathlib import Path # neatkarība on OS izmantot failu adresācijas
# Windows: r"\"
# MacOS / Linux: "/"

print(__file__)
current_dir = Path(__file__).parent
# "." - tagadēja direktorija
# __file__ - Python koda faila ceļš
# Path(__file__).parent - direktorija, kura atradas Python fails
# print(f"{current_dir.absolute() = }")
file_path = current_dir / "ikea_preces_3.xlsx"
# print(file_path.absolute())

dati = None

def load_file():
    global dati
    dati = pandas.read_excel(file_path)
    load_string.set("Fails ir ieladēts")
    print(dati.dtypes)
    print(dati.describe())

    skaitliski_dati = dati.select_dtypes(include=["float64", "int64"])
    print(skaitliski_dati.corr())

def draw_graph(dati):
    # global dati
    if load_string.get() == "Fails nav ieladēts":
    # if not dati:
        return
    else:
        graph_string.set("Grafiks tūlīt būs, uzgaidiet :)")
    # korelācijas parāda sakritītbu starp skaitliskām vērtībām
    sns.set_style("darkgrid")
    plt.rcParams["figure.figsize"] = (10, 8) # collās
    sns.heatmap(dati.corr(numeric_only=True), annot=True, cmap="coolwarm")
    # cmap = color map = krāsu skala
    # annot  = vai ir uzraksti ar vērtībām
    graph_string.set("Grafiks ir izveidots")
    plt.show()




logs = tk.Tk()
logs.geometry("400x300")

load_string = tk.StringVar(value="Fails nav ieladēts")
graph_string = tk.StringVar(value="Fails nav ieladēts, nevar veidot grafiku")

button_load = ttk.Button(logs, text="1. Atvērt failu", command=load_file)
button_graph = ttk.Button(logs, text="2. Uzzimēt grafiku", command=lambda: draw_graph(dati))

label_load = ttk.Label(logs, textvariable=load_string)
label_graph = ttk.Label(logs, textvariable=graph_string)

label_load.pack(pady=10)
button_load.pack(pady=10)
label_graph.pack(pady=10)
button_graph.pack(pady=10)


logs.mainloop()
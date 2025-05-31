# Vertību izgūšana no Widgets

# https://docs.python.org/3/library/tkinter.html
import tkinter as tk
from tkinter import ttk # Modernāks izskāts priekš GUI Widgets


def button_func():
    print("Sveiki! Poga bija nospiesta")

    entry_text = entry.get() # Izņēmt Entry saturu
    # print(f"Entry ievadīts: {type(entry_text)=}")
    string_mainigais.set(entry.get())
    print(string_mainigais.get(), type(string_mainigais))

    # Int ievadot tekstu bez cipariem būs kļūda (non fatal)
    # int_mainigais.set(entry_text)
    # print(int_mainigais.get(), type(int_mainigais))
    
    # Label atjaunināšana
    # button_label.configure(text=entry_text)
    # button_label["text"] = entry_text # pa taisno, bez Tkinter mainīgiem
    button_label["text"] = string_mainigais.get() # izmantojot Tkinter mainīgos, labaks paņemiens
    # entry["state"] = "disabled" # ievads tiek atslēgts


# 1. Izveidot programmas logu
logs = tk.Tk() # logs (window) - Galvenais el.
logs.title("Tkinter mainīgie") # loga nosaukums
logs.geometry("800x500") # loga izmērs "PlatumsxAugstums"

# 2. Aizpildīšana ar elementiem

# Tkinter mainīgais, priekš "korektākas datu izņemšanas"
string_mainigais = tk.StringVar(value="tests")
# value - sākuma (noklūsēta) vertība
int_mainigais = tk.IntVar()

# Label - tekst
label = ttk.Label(
    master=logs,
    text="Šīs ir tekta izvads - Label",
    font="Consolas 20 bold"
)
label.pack() # .pack() - widget novietojums uz loga, pēc noklusējuma

# Entry - ievads
entry = ttk.Entry(master=logs, textvariable=string_mainigais)
entry.pack()


# Button - poga
button = ttk.Button(
    master=logs,
    text="Pogas teksts",
    command=lambda: button_func()
)
button.pack()

# Label priekš pogas izvades:
button_label = ttk.Label(master=logs, text="Šeit būs Entry ievads...")
button_label.pack()

entry1 = ttk.Entry(master=logs, textvariable=string_mainigais)
entry1.pack()

# 3. Palaist
logs.mainloop() 

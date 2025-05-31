# Izmantojamais modulis tkinter, iebūvēts Python
# Alternatīvas:
#   PySimpleGUI - tagad diemžēļ par maksu...
#   PyQT5
#   PyKivi
#   u.c.

# https://docs.python.org/3/library/tkinter.html
import tkinter as tk
from tkinter import ttk # Modernāks izskāts priekš GUI Widgets
# caur 'ttk' var izsāukt:
#   - Label
#   - Entry
#   - Button
#   - Frame <- Widget, kurā var ievietot citus Widgets
#   - Checkbutton (ķeksis)
#   - Radiobutton (radio-poga) - var ievietot vairākus, bet izvelēties tikai vienu
#   - u.c.


# 1. Izveidot programmas logu
logs = tk.Tk() # logs (window) - Galvenais el.
logs.title("Programmas nosaukums") # loga nosaukums
logs.geometry("800x500") # loga izmērs "PlatumsxAugstums"

# 2. Aizpildīšana ar elementiem
# Visi zemāki el. piederes logam, vai citiem iepriekš definētiem el.
# Tkinter tie saucas par Widgets
# Label - tekst
label = ttk.Label(
    master=logs,
    text="Šīs ir tekta izvads - Label",
    font="Consolas 20 bold"
)
# font="<Fonta nosaukums> <fonta izmērs> <stils - bold/itallic>"
label.pack() # .pack() - widget novietojums uz loga, pēc noklusējuma


# Text - Tekst
text = tk.Text(master=logs)
text.pack()

# Entry - ievads
entry = ttk.Entry(master=logs)
entry.pack()

def button_func(kaut_kas):
    print("Sveiki! Poga bija nospiesta")
    print(f"Bija iedota vertība {kaut_kas}")

# Button - poga
button = ttk.Button(
    master=logs,
    text="Pogas teksts",
    command=lambda: button_func("Mans ievads") # lambda: - "mini funkcija", 
                                               # parasti izmantojas pie parametru izsaukšanās
)
# command=<funkcijas_nosaukums> - kura būs izsaukta pogas nospiešanas laikā
# funkcija nosaukums pierakstas bez iekavam - tikai tas definējums
button.pack()

# 3. Palaist
logs.mainloop() 
# .mainloop() :
#   - logs paliek atvērts
#   - ieslēdzas sadarbošana ar loga (Tk()) elemntiem.
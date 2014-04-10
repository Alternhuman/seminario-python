#!/usr/bin/env python
from Tkinter import *
import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(0.72 * value)
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="dolares").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="son equivalentas a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="euros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

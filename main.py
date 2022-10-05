import tkinter as tk

def callback(selection):
    global calculations
    calculations = selection

def calculate():
    global calculations
    val_1 = 0 if not entry_1.get() else float(entry_1.get())
    val_2 = 0 if not entry_2.get() else float(entry_2.get())

    if calculations == 'Addition':
        output.config(text=val_1 + val_2) ##Hier stehen geblieben.

window = tk.Tk()
window.geometry('700x400')

liste_optionen = ["Addition", "Subtraktion", "Multiplikation", "Division"]
variable = tk.StringVar(window)
variable.set('Select')

opt = tk.OptionMenu(window, variable, *liste_optionen, command=callback)
opt.config(font=('Helvetica', 12))
opt.grid(row=0, column=0)

entry_1 = tk.Entry(window)
entry_1.grid(row=0, column=1)

entry_2 = tk.Entry(window)
entry_2.grid(row=0, column=2)

button = tk.Button(window, text='Calculate', command=calculate)
button.grid(row=1, column=0)

output = tk.Label(window)
output.grid(row=2)

window.mainloop()
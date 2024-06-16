#使用 Radiobutton

import tkinter as tk
from tkinter import ttk

wnd = tk.Tk()
wnd.title('Radiobutton')

def myOptions():
    print('Your choice is :', var.get())

ft = ('Franklin Gothic Book', 14)
ttk.Label(wnd, text = """ 選擇你\n最愛的水果：""", font = ('Arial', 14),
      justify = 'center', padding = 20).pack()

fruits = [('Watermelon', 1), ('Pompelmous', 2),
          ('Strawberry', 3), ('Orange', 4),
          ('Apple', 5), ('Dragon fruit', 6)]
var = tk.IntVar()
var.set(3)
for item, val in fruits:    
      ttk.Radiobutton(wnd, text = item, value = val,
      variable = var, command = myOptions).pack(
      anchor = 'w', padx = 15, pady = 5)
wnd.mainloop()

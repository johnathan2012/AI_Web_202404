# Button的屬性state
import tkinter as tk
from tkinter import ttk

wnd = tk.Tk()
wnd.title('Button state...')

#屬性state的參數值
state = ['normal', 'active', 'disabled']

#for廻圈配合state參數值顯示按鈕狀態
for item in state:
    btn = ttk.Button(wnd, text = item, state = item)
    btn.pack()

wnd.mainloop()

#以geometry()方法設定主視窗物件的大小
import tkinter as tk
from tkinter import ttk

wnd = tk.Tk()         # 產生主視窗物件
wnd.title('CH1504')   # 標題列欲顯示的文字

# 設定主視窗的寬、高和顯示位置(x, y座標)
wnd.geometry('230x90+5+40')

ttk.Label(wnd, text = 'Label: First',
        background = 'skyblue').pack()
ttk.Label(wnd, text ='Label: Second',
        background = 'pink').pack()
wnd.mainloop()

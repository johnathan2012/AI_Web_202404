# Lable的使用
import tkinter as tk
from tkinter import ttk

wnd = tk.Tk() # 建立主視窗物件
wnd.geometry('235x240') 
wnd.title('使用Label')

photo = tk.PhotoImage(
   file = 'D:/PyCode/Demo/pic01.png')  # 建立圖片

# 使用Style()建構式，配合config()方法，設定左、右兩個標籤屬性
ttk.Style().configure('Left.Label', width = 8,
      justify = 'center', wrapLength = 120,
      foreground = '#000', relief = 'groove',
      background = '#DDD', font = ('Arial', 14))

ttk.Style().configure('Right.Label', width = 10,
      foreground = '#FFF', relief = 'ridge',
      background = '#777', font = ('標楷體', 20))

# 產生3個標籤
one = ttk.Label(wnd, text = 'Hello\nPython',
      style = 'Left.Label')
two = ttk.Label(wnd, text = '美麗世界', style = 'Right.Label')
three = ttk.Label(wnd, image = photo,
      relief = 'sunken', width = 150)

one.grid(row = 0, column = 0)
two.grid(row = 0, column = 1)
three.grid(columnspan = 2)   # 合併兩欄為一欄

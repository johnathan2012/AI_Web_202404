#使用pack()方法，參數expand
import tkinter as tk
from tkinter import ttk

root = tk.Tk()   # 產生主視窗物件
root.title('pack參數expand')

# 設定標籤的顯示文字(text)、背景(bg)和前景(fg)顏色
ttk.Label(root, text = 'Red', background = 'red', 
         foreground = 'white').pack(fill = tk.BOTH,
         side = 'left', expand = 1)   # 加入版面

ttk.Label(root, text = 'Green', background = 'green',
        foreground = 'white').pack(padx = 5, pady = 5)

ttk.Label(root, text = 'Blue', background = 'Blue',
        foreground = 'white').pack()
root.mainloop()

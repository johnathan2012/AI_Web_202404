#使用pack()方法，參數fill
import tkinter as tk
from tkinter import ttk

root = tk.Tk()   # 產生主視窗物件
root.title('pack()參數fill')

# 設定標籤的顯示文字(text)、背景和前景顏色, 加入版面
ttk.Label(root, text = 'Red', foreground = 'white',
          background = 'Red').pack(fill = tk.X)

ttk.Label(root, text = 'Green',
        background = 'green', foreground = 'white').pack()

ttk.Label(root, text = 'Blue',
        background = 'blue', foreground = 'white').pack()

root.mainloop()

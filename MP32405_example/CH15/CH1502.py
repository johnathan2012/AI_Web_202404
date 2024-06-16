import tkinter as tk
from tkinter import ttk

class appWork(tk.Tk):
   def __init__(self):
      super().__init__()     # super()方法呼叫Tk元件的相關方法
      self.title('CH1502')   # 顯示於視窗標題列

      # 第1個引數parent，以self取代
      lblShow = ttk.Label(self,
            text = 'Python is great fun!')

      # 指定Label向x, y兩個方向擴展(tk.BOTH)，增加x = 100, y = 50像素的空白
      lblShow.pack(fill = tk.BOTH, expand = 1,
            padx = 100, pady = 50)

# 產生主視窗物件
work = appWork()

# 視窗訊息初始化
work.mainloop()

# 一個簡單的視窗程式，兩個按鈕，左側按鈕顯示今天日期，右側按鈕結束應用程式

import tkinter as tk
from tkinter import ttk
from datetime import date

class wndApp(ttk.Frame): # 定義子類別，繼承了父類別Frame

   def __init__(self, ruler = None):
      ttk.Frame.__init__(self, ruler)
      self.pack()
      self.makeComponent()

   def makeComponent(self): # 建立兩個按鈕

      # 位於Frame左側按鈕, command呼叫dislply()方法
      self.atDay = ttk.Button(self,
            text = '我是 按鈕\n(Click Me ...)',
            command = self.display)
      self.atDay.pack(side = 'left')

      #位於Frame右側按鈕 - command呼叫destroy()方法來清除主視窗物件
      self.QUIT = ttk.Button(self, text = 'QUIT', command = wnd.destroy)
      self.QUIT.pack(side = 'right')

   def display(self):   # 定義方法，按一下滑鼠顯示今天日期
      today = date.today()
      print('Day is', today)

wnd = tk.Tk()         # 產生主視窗物件
wnd.title('CH1503')   # 標題列顯示文字
wndApp()
wnd.mainloop()   # 訊息呼叫

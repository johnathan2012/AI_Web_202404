# 使用Frame - relief屬性來顯示框線
import tkinter as tk
from tkinter import ttk

# relief常數值以list物件儲存
easyup = [tk.RAISED, tk.SUNKEN, tk.FLAT, tk.RIDGE, tk.GROOVE, tk.SOLID]

class appWork(ttk.Frame):
   def __init__(self, master = None):
      ttk.Frame.__init__(self, master)
        
      for item in easyup: #讀取relief常數值            
         fm = ttk.Frame(master, borderwidth = 2, relief = item)
         lblLeft = ttk.Label(fm, text = item, width = 5)
         lblLeft.pack(side = 'left')
            
         #加入版面，padx:元件之間的水平距離，pady: 垂直間距
         fm.pack(side = 'left', padx = 2, pady = 10)

def main():
   #產生物件
   work = appWork()
   # 顯示於視窗標題列
   work.master.title('CH1505 - relief 常數值')
   work.master.maxsize(1000, 400)
   # 視窗訊息初始化
   work.mainloop()

main()

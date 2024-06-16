#使用pack()方法，參數side
import tkinter as tk
from tkinter import ttk

class DemoPack:
   def __init__(self, parent):

      # 設定標籤的顯示文字(text)、背景和前景顏色，pack()加入版面
      lblOne = ttk.Label(parent, text = 'Red',
               background = 'red', foreground = 'white')
      lblOne.pack(side = 'right', padx = 5)   # 加入版面

      lblTwo = ttk.Label(parent, text = 'Green',
            background = 'green', foreground = 'white')
      lblTwo.pack(side = 'right', padx = 5, pady = 10)

      lblThree = ttk.Label(parent, text = 'Blue',
            background = 'blue', foreground = 'white')
      lblThree.pack(side = 'right')

def main():
   root = tk.Tk()
   root.title('pack()_參數side')   # 設定標題列
   root.geometry('200x80')
   showApp = DemoPack(root)
   root.mainloop()

main()

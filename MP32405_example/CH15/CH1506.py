#使用pack()方法，無參數，三個元件會依序擺在視窗的中央
import tkinter as tk
from tkinter import ttk

class DemoPack:
   def __init__(self, parent):
      # 設定標籤的顯示文字(text)、設背景和前景顏色，pack()加入版面
      ttk.Label(parent, text = 'Red',
            background = 'Red', foreground = 'White').pack()
      ttk.Label(parent, text = 'Green',
            background = 'Green', foreground = 'White').pack()
      ttk.Label(parent, text = 'Blue',
            background = 'Blue', foreground = 'White').pack()

def main():
   root = tk.Tk()
   root.title('無參數pack()')   # 設定標題列
   root.geometry('220x80')
   showApp = DemoPack(root)
   root.mainloop()

main()

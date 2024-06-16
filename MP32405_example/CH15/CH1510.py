# 以grid()方法設定欄、列，將元件做版面配置
import tkinter as tk
from tkinter import ttk

class showApp:
   def __init__(self, root):
      
      self.word = tk.StringVar()   # StringVar()方法處理字串
      self.w1 = tk.StringVar()
      self.w2 = tk.StringVar()

      # 標籤設第1、2列位置
      lblFirst = ttk.Label(root, text = 'First')
      lblFirst.grid(row = 0, column = 0, sticky = 'w')
      lblSecond = ttk.Label(root, text = 'Second')
      lblSecond.grid(row = 1, column = 0, sticky = 'w')

      # 顯示結果的標籤
      lblResult = ttk.Label(root, textvariable = self.word)
      lblResult.grid(row = 2, column = 1)

      # Entry()建構式產生單行文字方塊
      one = ttk.Entry(root, width = 10, textvariable = self.w1)
      one.grid(row = 0, column =1)
      two = ttk.Entry(root, width = 10, textvariable = self.w2)
      two.grid(row = 1, column =1)
      one.focus()   # 取得輸入焦點

      # 按鈕
      btnShow = ttk.Button(root, text = '顯示', command = self.show)
      btnShow.grid(row = 2, column = 0)

   def show(self, *args):   # 定義函式，回應按鈕的訊息
      value = self.w1.get() + self.w2.get()
      self.word.set(value)

def main():
   wnd = tk.Tk()   # 產生主視窗物件
   showApp(wnd)    # 主視窗物件再由類別傳入
   wnd.title('grid()方法')
   wnd.mainloop()

main()

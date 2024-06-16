# 以grid()方法設定欄、列，將元件做版面配置
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('grid()方法')

def show(*args):   # 定義函式，回應按鈕的訊息
   value = w1.get() + w2.get()
   word.set(value)

word = tk.StringVar()
w1 = tk.StringVar()
w2 = tk.StringVar()

# 標籤設第1、2列位置
ttk.Label(root, text = 'First').grid(
   row = 0, column = 0, sticky = 'w')
ttk.Label(root, text = 'Second').grid(
   row = 1, column = 0, sticky = 'w')

# 顯示結果的標籤
ttk.Label(root, textvariable = word).grid(
   row = 2, column = 1)

# Entry()建構式產生單行文字方塊
one = ttk.Entry(root, width = 10, textvariable = w1)
one.grid(row = 0, column =1)
two = ttk.Entry(root, width = 10, textvariable = w2)
two.grid(row = 1, column =1)

# 按鈕
btnShow = ttk.Button(root, text = '顯示', command = show)
btnShow.grid(row = 2, column = 0)

one.focus()   # 取得輸入焦點
root.mainloop()

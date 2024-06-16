# messagebox的方法
import tkinter as tk
from tkinter import messagebox

root = tk.Tk().withdraw() # 隱藏主視窗物件

info = messagebox.askokcancel('Create File', '是否要寫入檔案')
filename = '../Demo/demo1402.txt'

with open(filename, 'w') as fin:
    fin.write(str(info))
    print(str(var) + ' File Name: ' + filename)

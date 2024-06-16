import tkinter as tk
from tkinter import ttk

''' 以place()方法，將兩個Frame 進行版面配置
    relief: FLAT, SUNKEN, RAISED, GROOVE, and RIDGE
'''

wnd = tk.Tk()             # 建立主視窗物件
wnd.title('水平分割')
wnd.geometry('200x150')   # 設主視窗大小
wnd.resizable(0, 0)       # 無法自行調整視窗大小


#產生Frame，呼叫place()方法，透過split值做水平分割
f1 = ttk.Frame(wnd, borderwidth = 5, relief = 'groove')

split = 0.4 # 分割值
f1.place(rely = 0, relwidth = 1, relheight = split)

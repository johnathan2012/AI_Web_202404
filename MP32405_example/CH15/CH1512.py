import tkinter  as tk
from tkinter import ttk

wnd = tk.Tk()             # 建立主視窗物件
wnd.geometry('250x100')   # 設視窗大小250X100
wnd.title('place()方法')

#標籤 - 設背景色
t1 = ttk.Label(wnd, text = 'First', background = 'white',)
t2 = ttk.Label(wnd, text = 'Second', background = 'LightGray',)

# 呼叫place()方法，屬性relx相對於視窗X座標(0.2)
t1.place(relx = 0.2, x = 0, y = 2,
         width = 120, height = 28)
t2.place(relx = 0.2, x = 1, y = 35,
         width = 120, height = 28)

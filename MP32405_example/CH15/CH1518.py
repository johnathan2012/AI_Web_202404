#使用Checkbutton - 多選鈕

import tkinter as tk
from tkinter import ttk

wnd = tk.Tk()
wnd.title('Checkbutton')

def varStates(): # 回應核取方塊變數狀態
   value = f'{var1.get()} {var2.get()} {var3.get()}'
   inst.set(value)

inst = tk.StringVar()   # 顯示勾選項目
var1 = tk.StringVar()   # 勾選 音樂 項目
var2 = tk.StringVar()   # 勾選 閱讀 項目
var3 = tk.StringVar()   # 勾選 爬山 項目
item1, item2, item3 = '音樂', '閱讀', '爬山'

# 產生標籤並以grid()方法加入版面
label1 = ttk.Label(wnd, text = '興趣')
label2 = ttk.Label(wnd, text = '興趣，有->')
label3 = ttk.Label(wnd, textvariable = inst)
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)
label3.grid(row = 1, columnspan = 3)

# 產生Checkbutton元件，grid()方法加入版面
chk = ttk.Checkbutton(wnd, text = item1,
    variable = var1, onvalue = item1, offvalue = '')
chk2 = ttk.Checkbutton(wnd, text = item2, 
    variable = var2, onvalue = item2, offvalue = '')
chk3 = ttk.Checkbutton(wnd, text = item3,
    variable = var3, onvalue = item3, offvalue = '')
chk.grid(row = 0, column = 1)
chk2.grid(row = 0, column = 2)
chk3.grid(row = 0, column = 3)

# 產生按鈕並加入版面
btnQuit = ttk.Button(wnd, text = 'Quit', command = wnd.destroy)
btnShow = ttk.Button(wnd, text = 'Show', command = varStates)
btnQuit.grid(row = 3, column = 1, pady = 4)
btnShow.grid(row = 3, column = 2, pady = 4)

wnd.mainloop()

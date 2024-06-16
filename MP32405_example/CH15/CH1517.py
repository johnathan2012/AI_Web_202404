# Label顯示秒數，按下Button停止
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('秒數計算中...')
root.geometry('100x100+150+150')#視窗大小

counter = 0 # 儲存數值

def display(label):    # 接收標籤
    counter = 0
    def count():       # 進行計數
        global counter # 全域變數
        counter += 1
        label.config(text = str(counter),
            background = 'Gray', width = 20)
        label.after(1000, count)
    count()
  
show = ttk.Label(root, foreground = 'White')
show.pack()
display(show)

# 建立按鈕，按下時呼叫destory()方法來清除視窗物件
btnStop = ttk.Button(root, text = 'Stop',
    width = 20, command = root.destroy)
btnStop.pack()

root.mainloop()

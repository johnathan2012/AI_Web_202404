# messagebox的_show()方法
import tkinter as tk
from tkinter import messagebox

root = tk.Tk().withdraw() # 隱藏主視窗物件

messagebox._show('CH15', '發生錯誤，是否繼續？',
    'error', 'abortretryignore')

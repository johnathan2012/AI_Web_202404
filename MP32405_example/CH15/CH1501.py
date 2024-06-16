import tkinter as tk
from tkinter import ttk   # Step 1

root = tk.Tk()   # Step 2.建立主視窗

# Step 3.加入標籤，設定屬性值
lblShow = ttk.Label(root, text = 'Hello Python!!')

lblShow.config(width = 20, foreground = 'White',
   background = 'LightGray', font = ('Arial', 18))

# Step 4.呼叫此方法納入版面管理，Label才會顯示於主視窗
lblShow.pack()

# Step 5.產生訊息廻圈
root.mainloop()

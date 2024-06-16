from tkinter import *
from tkinter import ttk

def calcuMeters(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title('單位換算')

appWork = ttk.Frame(root, padding = '3 3 12 12')
appWork.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

feet, meters = StringVar(), StringVar()
#meters = StringVar()

ttk.Label(appWork, text = 'feet').grid(
   column = 1, row = 1, sticky = W)
ttk.Label(appWork, text = '相當於').grid(
   column = 1, row = 3, sticky = E)
ttk.Label(appWork, text = '公尺').grid(
   column = 3, row = 3, sticky = W)
# 輸出換算結果
ttk.Label(appWork, textvariable = meters).grid(
   column = 2, row = 3, sticky = (W, E))

# 單行文字方塊取得feet輸入值
ftInput = ttk.Entry(appWork, width = 7, textvariable = feet)
ftInput.grid(column = 2, row = 1, sticky = (W, E))

ttk.Button(appWork, text= '換算',
   command = calcuMeters).grid(
   column = 2, row = 2, sticky = W)

for child in appWork.winfo_children(): 
    child.grid_configure(padx = 5, pady = 5)

ftInput.focus()   # 取得輸入焦點
root.bind("<Return>", calcuMeters)

root.mainloop()

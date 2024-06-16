#使用Entry取得輸入文字

from tkinter import *
from tkinter import ttk

class workApp():
   def __init__(self, root):
      root.title('Entry 元件')

      self.data = StringVar()
      self.pwd = StringVar()

      frMain = ttk.Frame(root, padding = '3 3 5 5')
      frMain.grid(column = 0, row = 0, sticky = (N, W, E, S))
      self.makeComponent(frMain)

   def makeComponent(self, frMain):   # 定義方法，設定標籤、文字方塊和按鈕
      lblOne = ttk.Label(frMain, text = '通關密語:',
               font = ('標楷體', 14))
      lblTwo = ttk.Label(frMain, textvariable = self.pwd)
      inputPwd = ttk.Entry(frMain, show = '*',
            textvariable = self.data, width = 11)
      btnSend = ttk.Button(frMain, text = '確認',
            command = self.callBack)

      # grid()方法配置版面
      lblOne.grid(row = 0, column = 0, sticky = W)
      inputPwd.grid(row = 0, column = 1, sticky = E)
      btnSend.grid(row = 1, column = 0, sticky = (W, E))
      lblTwo.grid(row = 1, column = 1, sticky = E)

      inputPwd.focus()   # 取得輸入焦點

   def callBack(self, *args):   # 定義方法取得Button的Command訊息
      value = self.data.get()
      self.pwd.set('密碼 ' + value) 

wnd = Tk()   # 建立主視窗物件
workApp(wnd)
wnd.mainloop()

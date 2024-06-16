# 改寫範例《CH1101.py》，加入__init__()方法

class Motor:   # 定義類別
   def __init__(self, name, color):
      self.name = name
      self.color = color
   
   #定義方法二：輸出名稱和顏色
   def showMessage(self):
      print(f'款式:{self.name:>6s}, 顏色:{self.color:4s}')

car = Motor('Vios', '極光藍')
car.showMessage()

# 使用 @classmethod, @staticmethod

class Motor:

   count = 0             # 類別屬性統計物件
    
   def __init__(self):
      Motor.count += 1   # 計算物件個數
       
   @classmethod          # 類別方法
   def equip(cls, rmp, seats):   # cls為類別本身
      print('排氣量', rmp, '座位數', seats)
        
   @staticmethod   # 靜態方法
   def display():
      print('有', Motor.count, '個物件')

car = Motor()        # 產生第1個物件
car.equip(1500, 4)   # 以物件呼叫方法

hybird = Motor()     # 第2個物件
hybird.equip(2000, 7)

juddy = Motor()      # 第3個物件
Motor.equip(1800, 5) # 類別呼叫方法

Motor.display()      # 統計物件數


class Motor:     # 定義類別
   @staticmethod # 將equip()方法修飾為靜態方法
   def equip(name, seats):
      print('車款', name, '座位數', seats)

car = Motor()#產生物件
Motor.equip('SUV', 7)# 以類別呼叫類別方法
car.equip('altis', 4)# 以物件呼叫物件方法

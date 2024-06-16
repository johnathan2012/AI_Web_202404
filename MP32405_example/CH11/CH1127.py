class Increase:#定義類別
   def __init__(self, num = 0):   # 初始化物件
      self.value = num

   def __add__(self, num):        # 兩數相加
      return self.value + num

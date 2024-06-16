#子類別覆寫父類別的方法

class Mother():   # 父類別
   def display(self, pay):
      self.price = pay
      if self.price >= 30000:
         return pay * 0.9
        
class Son(Mother):           # 子類別
   def display(self, pay):   # 覆寫display方法
      self.price = pay
      if self.price >= 30000:
         print('8折：', end = ' ')
         return pay * 0.8

Joe = Son()#建立物件
print(Joe.display(35000))

#定義多形
class Motor(): #父類別
   def __init__(self, name, price):
      self.name = name
      self.price = price

   def equip(self):
      return self.price
    
   def show(self):
      return self.name
    
class sportCar(Motor):#子類別
   def equip(self):        
      return self.price * 1.15 
    
class Hybrid(Motor): #子類別
   def equip(self):
      return self.price *1.2


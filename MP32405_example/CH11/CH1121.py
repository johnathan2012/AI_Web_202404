# 將原有的Motor類別變更為類別裝飾器

class Motor: #以類別為裝飾器

   def __init__(self, func):
      self.func = func
        
   def __call__(self, *args):
      for arg in args:
         print(arg, end=' ')
      print()

@Motor #下面敘述等同於 Motor = Equip(Motor)
def Equip(arg):
   pass

veh1 = Equip('Yaris') #呼叫__call__()方法
veh2 = Equip('Altis', 1800)
veh3 = Equip('Hybrid', 2000, '極緻黑')

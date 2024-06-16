# 把定義的類別當作裝飾器

class Motor:
   def __call__(self, *args):
      for arg in args:
         print(arg, end=' ')
      print()

#*args收集位置引數，所以參數可長可短
vehicle = Motor()#產生物件
vehicle('Yaris')
vehicle('Altis', 1800)
vehicle('Hybrid', 2000, '極緻黑')

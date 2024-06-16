import math
# 定義類別
class Circle:
   '''
       定義類別的方法
       calcPerimeter : 計算圓周長
       roundArea     : 計算圓面積
       __init__()    : 自訂物件初始化狀態
   '''

   #__init__ 初始化物件 
   def __init__(self, radius = 15):
      self.radius = radius

   def calcPerimeter(self):   # 定義方法計算圓周長
      return 2 * self.radius * math.pi

   def roundArea(self):   # 定義方法來計算圓面積
      return self.radius * self.radius * math.pi

# 產生物件
r1 = Circle(12)
print('圓的半徑:', r1.radius)

periphery = r1.calcPerimeter()
print('圓周長:', periphery)

area = r1.roundArea()
print('圓面積:', area)
# print(Circle.__doc__)   #輸出類別內長文件註解


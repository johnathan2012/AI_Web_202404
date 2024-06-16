# raise敘述 配合內建異常型別
import math

# 定義函式
def calcArea(radius):
   if radius < 0:
      raise RuntimeError("不能輸入負值")
   else:
      area = radius * radius * math.pi
      return area

#呼叫函式
value = float(input('請輸入數值: '))
circleArea = calcArea(value)
print('圓面積', circleArea)

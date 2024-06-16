# 定義裝飾器函式
def outerNums(func):
   def inner(x, y):   # 接收參數
      x, y = eval(input('Two numbers:'))
      return func(x, y)
   return inner

@outerNums   # 裝飾器
def plusNumbers(x, y):
    return x**2 + y**2

@outerNums
def minusNumbers(x, y):
    return x**2 - y**2

a, b = 0, 0
print('平方和:', plusNumbers(a, b))
print('平方差:', minusNumbers(a, b))

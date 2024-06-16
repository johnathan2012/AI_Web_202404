#使用__gt__()、__lt__()、__eq__()做比較

class Comp:
   data = 743
   def __gt__(self, value):# x > y
      return self.data > value

   def __lt__(self, value): # x < y
      return self.data < value

   def __eq__(self, value): # x == y
      return self.data == value

A = Comp()
print('回傳值：', A > 8865)
print('回傳值', A < 253)
print('回傳值', A == 743)

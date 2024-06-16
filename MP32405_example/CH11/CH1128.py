'''
   重載運算子 __add__()，'+'左側運算元必須是物件
   重載運算子 __radd__()， '+'左側運算元可以是數值
'''

class Increase: #定義類別
   def __init__(self, num = 0):   # 初始化物件
      self.value = num
        
   def __add__(self, num):   # 兩數相加
      print(f'Add is {self.value} + {num}')
      return self.value + num

   def __radd__(self, num):   # 允許左側元可以是數值
      print('radd is {} + {}'.format(self.value, num))
      return num + self.value

n1 = int(input('Input Numbers:'))
number = Increase(n1)
print(f'{n1} + 12 = {number + 12}')
print('12 + ', n1, '=', 12 + number)


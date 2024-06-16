#重載方法__add__()、__sub__()

class Arithm:

   def __init__(self, num):
      self.value = num      

   def __add__(self, num): # 相加
      return Arithm(self.value + num)

   def __sub__(self, num): # 相減
      return Arithm(self.value - num)

one = Arithm(255)
result = one + 20
print('相加：', result.value)
result = one - 144
print('相減：', result.value)

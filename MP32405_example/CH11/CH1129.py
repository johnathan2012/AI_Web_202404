'''
   重載運算子 __add__()，'+'左側運算元必須是物件
   重載運算子 __radd__()， '+'左側運算元可以是數值
   BIF isinstance()來判斷傳入的參數是否為物件
'''

class Increase: #定義類別
    def __init__(self, num = 0):   # 初始化物件
        self.value = num
        
    def __add__(self, num):        # 兩數相加
        if isinstance(num, Increase):
            num = num.value        
        return Increase(self.value + num)

    def __radd__(self, num):       # 允許左側元可以是數值        
        return num + self.value        
    
    def __str__(self):        
        return '= %d' % self.value
    
n1, n2 = eval(input('Two Numbers: '))
A = Increase(n1)
B = Increase(n2)
print(n1, '+', 35, A + 35)
print(n2, '+', 127, B + 127)

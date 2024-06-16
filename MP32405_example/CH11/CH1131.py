#重載運算子 __add__()和__sub__()

class Effectua1:
    def __init__(self, num): # 初始化，傳入數值
        self.data = num
    def __add__(self, num):#相加, overload '+'
        #回傳一個新的實體
        return Effectua1(self.data + num)
    def __sub__(self, num): #相減        
        return Effectua1(self.data - num)

n1, n2 = eval(input('Two Numbers:'))
one = Effectua1(n1) # Effectua1.__init__(one, 5)
result = one + 12 #Effectua1.__add__(one, 2)
print(n1, '+ 12 = ', result.data)
two = Effectua1(n2)
result = two - 17
print(n2, '- 17 = ', result.data)

#定義可原地相加的__iadd__()方法

class Increase: #定義類別
    def __init__(self, num = 0):   # 初始化物件
        self.value = num
        
    def __add__(self, num):   # a += b
        self.value += num        
        return self    

#產生物件
n1, n2 = eval(input('Two number:'))
A = Increase(n1)
A += n2
print('A +=', n2, '結果：', A.value)

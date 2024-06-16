# Local function的概念

def exter(x, y):   # 函式中有函式

    def internal(a, b):
        #BIF divmod() a//b, a % b 
        return divmod(a, b)
    return internal(x, y)

#呼叫函式
print(exter(25, 7))

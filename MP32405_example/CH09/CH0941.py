# 產生費氏數列
def fiboA(num):
    result = [] #儲存費氏數列
    a, b = 0, 1
    while b < num:
        result.append(b) 
        a, b = b, a + b
    return result

#呼叫函式
print('Fibonacci:', fiboA(10))

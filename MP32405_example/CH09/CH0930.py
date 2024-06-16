# 在函式中去呼叫另一個函式

def multip(num1, num2):   # 函式一
    print('兩數相乘', num1 * num2)

# 函式二有3個參數
def handle(func, one, two):
    func(one, two)

#呼叫函式
handle(multip, 4, 7)

# 函式參數為*星號運算式

def calcu(*value):
    result = 1
    for item in value:
        result *= item
    return result

#呼叫函式
print('1個引數:', calcu(7)) #無任何引數
print('3個引數:', calcu(2, 3, 5)) #3個引數

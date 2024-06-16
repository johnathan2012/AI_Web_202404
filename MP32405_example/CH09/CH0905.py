# 如果回傳值有多個，return敘述可以配合Tuple物件來表達

def answer(x, y):   # 定義函式
    return x+y, x*y, x/y
    
#呼叫函式
numA = int(input('輸入第一個數值:'))
numB = int(input('輸入第二個數值:'))

# 儲存回傳的值
data = answer(numA, numB)

# 以f-string做格式化處理
print(f'運算結果: {data[0]}, {data[1]:,}, {data[2]:,.10f}')

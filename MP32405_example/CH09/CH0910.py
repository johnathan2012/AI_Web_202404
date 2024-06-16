# 預設參數值與可變、不可變物件

def number(A, B = []):
    B.append(A)
    print(B)

# 呼叫函式
number(2)    # 輸出[2]
number(5)    # 輸出[2, 5]
number(12)   # 輸出[2, 5, 12]

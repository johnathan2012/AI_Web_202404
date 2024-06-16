# 位置參數須在預設參數值之前

def Demo(A, B = 7, C = 11):   #定義函式
    return A ** B // C   # 回傳計算結果

# 呼叫函式，只傳入一個引數，千位符號為逗號
print(f'一個引數: {Demo(6):,}')

# 呼叫函式，只傳入三個引數，千位符號為_底線字元
print(f'三個引數: {Demo(11, 12, 13):_}')   

# 定義計算階乘的函式
def fact(x):
    upshot = 1    # 儲存階乘計算結果
    for item in range(1, x+1):
        upshot *= item    # 累積相乘結果
    return upshot

#呼叫函式
print(f'{fact(8):_}')    # 千位符號使用_字元

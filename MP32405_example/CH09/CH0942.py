# 遞廻
def fibon(x):
    if x <= 1:   # 基本情況
        return x
    else:
        return fibon(x - 1) + fibon(x-2)   # 遞廻情況

#呼叫函式
outcome = [] #空串列
for item in range(10):
    outcome.append(fibon(item))
print('遞迴:', outcome)

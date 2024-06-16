# 使用try/except敘述 - 空的except敘述

number = 25, 67, 12 #Tuple

try:
    print(number[3])
except:  # 無任何Exception型別來處理
    print('索引超出界值')

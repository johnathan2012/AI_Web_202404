# 使用try/except敘述 - 加入Except類別

number = 25, 67, 12 #Tuple

try:
    print(number[3])
except Exception:
    print('索引超出界值')

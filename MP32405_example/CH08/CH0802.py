# Set & or 交集運算

num1 = {23, 24, 26}       # 準備集合1
num2 = {23, 24, 33, 45}   # 準備集合2

print(num1 & num2)        # 運算子& 交集計算

num1.intersection(num2)          # num1 & num2
print(num1.intersection((24, 33, 98)))  # 以Tuple為交集對象

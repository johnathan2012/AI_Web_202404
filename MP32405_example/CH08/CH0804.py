# Set ^ or 對等差集運算

num1 = {23, 24, 26}       # 準備集合1
num2 = {23, 24, 33, 45}   # 準備集合2

print('集合1', num1)
print('集合2', num2)

# 對等差集計算，運算是(num1 - num2) | (num2 - num1)，輸出{26, 33, 45}
print('num1 ^ num2 = ', num1 ^ num2)

result = num1.symmetric_difference(num2)   # 輸出{33, 26, 45}
print('對等差集運算', result)
print(num1.symmetric_difference([78, 24]))

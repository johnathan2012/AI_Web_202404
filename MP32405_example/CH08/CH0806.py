# 加強版交集運算，呼叫intersection_update方法，或者使用運算子&=

num1 = {11, 12, 13}       # Set物件
num2 = {22, 12, 13, 28}   # Set物件

print('num1 = ', num1)
print('num2 = ', num2)

num1 &= num2   # 加強版交集運算
num1.intersection_update(num2)   # 呼叫方法做加強版交集運算
print('加強版交集運算 > num1 &= num2 ', num1)   # 輸出{12, 13}

# 加強版差集運算，呼叫difference_update方法，或者使用運算子-=

num1 = {11, 12, 13, 15}   # Set物件
num2 = {28, 15, 12, 14}   # Set物件

print('num1 = ', num1)
print('num2 = ', num2)

# 加強版差集運算，呼叫方法
num1.difference_update(num2)    # 呼叫方法做加強版差集運算
print('加強版差集運算 > ', num1)   # 以num1為主，輸出{11, 13}

num1 = {11, 12, 13, 15}   # Set物件
num2 = {28, 15, 12, 14}   # Set物件
num2 -= num1   # 加強版差集運算，使用「-=」運算子
print('num2 -= num1 >', num2)   # 以num2為主，輸出{28, 14}

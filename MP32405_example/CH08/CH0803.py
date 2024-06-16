# Set - or 差集運算

num1 = {23, 24, 26}       # 準備集合1
num2 = {23, 24, 33, 45}   # 準備集合2

# 差集計算，輸出以num1為主的項目，所以是{26}
print(num1 - num2)

# 差集計算，輸出以num2為主的項目，所以是{33, 45}
print(num2 - num1)

print(num1.difference(num2))    #輸出{26}
print(num2.difference(num1))    #輸出{45, 33}

print(num1.difference([78, 26, 91]))    #輸出{24, 23}
print(num2.difference((33, 35, 21)))    #輸出{24, 45, 23}


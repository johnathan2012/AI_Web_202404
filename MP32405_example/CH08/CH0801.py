# Set | or 聯集運算

num1 = {23, 24, 26}       # 準備集合1
num2 = {23, 24, 33, 45}   # 準備集合2

print(num1 | num2)        # 運算子| 聯集計算

num1.union(num2)          # num1 | num2
print(num1.union([11, 18, 15]))  # 以List為聯集對象
print(num1.union('One', ('Two', 25)))   #可以多個參數

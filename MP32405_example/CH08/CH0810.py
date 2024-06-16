# 判斷集合裡是否有共同元素, 方法isdisjoint()
   
num1 = {11, 12}
num2 = {13, 14}
num3 = {12, 13}

print('num1 =', num1)
print('num2 =', num2)
print('num3 =', num3)

# num1, num2有無共同元素

print('num1, num2有無共同元素？', num1.isdisjoint(num2))

# num2, num3有一個共同元素
num1.issubset(num2)
print('num2, num3是否有共同元素？', num2.isdisjoint(num3))


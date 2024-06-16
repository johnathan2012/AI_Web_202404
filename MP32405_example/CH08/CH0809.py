'''
   判斷父、子集合, 方法issuperset() 或 運算子>=
   方法issubset() 或運算子<=
'''

num1 = {11, 12, 13, 14}
num2 = {12, 13}

print('num1 =', num1)
print('num2 =', num2)

# num1是否為num2父集合
num1.issuperset(num2)
print('num1是否為num2父集合？')
print('num1 >= num2 >', num1 >= num2)

# num1是否為num2子集合
num1.issubset(num2)
print('num1是否為num2子集合？')
print('num1 <= num2 >', num1 <= num2)

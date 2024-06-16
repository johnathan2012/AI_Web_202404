# 兩數相加
def plusNumbers(x, y):
    return x**2 + y**2

# 兩數相減
def minusNumbers(x, y):
    return x**2 - y**2

a, b = eval(input('Two numbers:'))

print('兩數平方和:', plusNumbers(a, b))
print('兩數平方差:', minusNumbers(a, b))

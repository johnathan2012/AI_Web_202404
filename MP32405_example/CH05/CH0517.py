# 方法join()、split()

num = ['One', 'Two', 'Three', 'Four']   # List物件
print('原來字串', num)
number = ', '.join(num)
print('字串結合->', number)   # 輸出'One, Two, Three, Four'
num2 = number.split(', ')
print('再次分割->', num2)
print(f'num == num2 -> {num== num2}')

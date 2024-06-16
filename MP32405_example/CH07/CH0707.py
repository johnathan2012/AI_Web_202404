# 使用setdefault()來防止找不到key

num1 = { 1: 'One', 2 : 'Two', 3 : 'Three'}

# 若 key 2存在，回傳value
print(f'key 2, value = {num1.setdefault(2)}')

# 若 key 4不存在，以此新增項目
print(f'key 4, value = {num1.setdefault(4, "Four")}')
# 若 key 5不存在，以None回傳
print(f'key 5, value = {num1.setdefault(5)}')

for item in num1:
   print(f'{item:2d} {num1[item]}')

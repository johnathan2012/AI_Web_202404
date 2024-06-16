import copy # 滙入copy模組，做淺層複製

num1 = [10, 20] # 一般List
num2 = copy.copy(num1) # 做複製
print(f'{num1}, {num2}') # 輸出相同元素

ary = [11, [22, 44], 33, 36, 39] # List中有List
target = copy.copy(ary)
print(f' ary == target, {ary == target}')

# ary和target均指向同一個物件參照
ary[0] = 33
print('ary第一個元素被改變')
print(f'{ary} \n{target}')   # 只有ary第一個元素被改變

target[1][0] = 125
print('ary, target皆有改變')
print(f'{ary} \n{target}')   # ary, target都被改變

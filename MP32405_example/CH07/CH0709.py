# 使用關鍵字引數    
week = dict(Sun = 1, Mon = 2, Tue = 3, Wed = 4)
print('隨意字典:'); print(week)

# 以串列取得key, value
keys = [1, 2, 3, 4] # 含有key的List
values = ['Sun', 'Mon', 'Tue', 'Wed']

# zip()函式組合
weekB = dict(zip(keys, values))
print('字典重新組合:'); print(weekB)

# for廻圈讀取
print('鍵/值：')
for key, value in weekB.items():
    print(f'{key:2d}:{value:4s}', end = '')
print()

print('<鍵>', end = '')
for key in weekB.keys():
    print(f'{key:4d}', end = '')
print('\n<值>', end = '')
for value in weekB.values():
    print(value, end = ' ')

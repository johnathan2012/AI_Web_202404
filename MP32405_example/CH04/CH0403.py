# 巢狀for產生九九乘表法，建立表頭
print('  |', end = '')
for k in range(1, 10):
   #不自動換行，只留空白字元
   print(f'{k:3d}', end = '') 
print() #換行
print('-' * 32)

# 第一層 for/in
for one in range(1, 10):
   print(one, '|', end = '')
   # 第二層 for/in
   for two in range(1, 10):
      print(f'{one * two:3d}', end = '')
   print() #換行



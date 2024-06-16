# break, continue敘述

total = number = 0 #儲存累加值

for item in range(2, 20):
   if item % 2 == 1:
      continue   # 只中斷此次廻圈，回到上一層for廻圈繼續執行
   total += item
   print(item, total)
else:
   print('偶數加總完畢')

for item in range(2, 20):
   
   if item % 10 == 0:
      break   # 中斷廻圈, 不再執行
   number += item
   print(item, number)
      

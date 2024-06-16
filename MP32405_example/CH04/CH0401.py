# for廻圈配合range函式做數字1~10加總

total = 0

for count in range(1, 10): # 數字1~10
   total += count          # 把數值累加
   print('累加值', total)   # 輸出累加結果
else:
   print('已加總完畢...')

# for廻圈配合range函式做數字奇數累加

total = 0

# 以奇數1, 3, 5做累加
for count in range(1, 100, 2):
   total += count          # 把數值累加
print('累加值', total)   # 輸出累加結果

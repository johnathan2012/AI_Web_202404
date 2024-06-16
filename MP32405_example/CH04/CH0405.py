number, total = 24831, 0

print('number remainder total') #標頭

# number的值大於零，進入廻圈
while number > 0:
   remain = number % 10   # 儲存餘數值
   total += remain # 儲存餘數值
   number //=10    # 只取整除值
   print(f'{number:6d}{remain:8d}{total:7d}')
    
print('餘數值 -> ', total)

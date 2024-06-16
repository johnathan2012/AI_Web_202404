# in運算子來確認元素是否存在

temp = input('輸入含有符號的溫度 -> ')

# 做溫度轉換
if temp[-1] in ['c', 'C']:
   #含有c或C的數值，就轉換為華式溫度
   fahr = 1.8 * eval(temp[0:-1]) + 32
   print(f'{temp} = {fahr:.2f}°F')
elif temp[-1] in ['f', 'F']:
   #含有f或F的數值，就轉換為攝式溫度
   cen = (eval(temp[0:-1]) -32) / 1.8
   print(f'{temp} = {cen:.2f}°C')
else:
   print('資料輸入有誤...')


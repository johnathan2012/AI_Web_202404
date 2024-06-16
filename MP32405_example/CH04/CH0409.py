'''
   修改範例0304，加入while廻圈來重覆執行
   以邏輯概念來檢查輸入的西元紀年是否為閏年
'''

year = int(input('請輸入西元紀年：'))

while year != 0:
   # 利用%運算子 配合邏輯運算子
   if (year % 4 == 0 and year % 100 != 0)\
         or (year % 400 == 0):
      print(year, '是閏年')
   else:
      print(year, '不是閏年')
   year = int(input('請輸入西元紀年：'))
else:
   print('執行完畢！')

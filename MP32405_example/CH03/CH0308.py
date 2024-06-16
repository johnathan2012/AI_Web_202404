'''
   修改範例0304，以巢狀if/else敘述改寫
   檢查輸入的西元紀年是否為閏年
'''

year = int(input('請輸入西元紀年：'))

# 利用%運算子判斷數值是否能整除
if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
         print(year, '--閏年--')
      else:
         print(year, '--非閏年--')
   else:
      print(year, '是閏年')
else:
   print(year, '不是閏年')

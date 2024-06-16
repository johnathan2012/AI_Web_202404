'''
   修改範例0308，以if/elif/else敘述改寫
   檢查輸入的西元紀年是否為閏年，由400整除開始做判斷
'''

year = int(input('請輸入西元紀年：'))

# 利用%運算子判斷數值是否能整除
if year % 400 == 0:
   print(year, '--閏年--')
elif year % 100 == 0:
   print(year, '--非閏年--')
elif year % 4 == 0:
   print(year, '是閏年')
else:
   print(year, '不是閏年')

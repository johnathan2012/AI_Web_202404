# if/elif/else 判斷月份

month = int(input('請輸入月份-> '))
if month == 3 or month == 4 or month == 5:
   print(month, '月是春天')
elif month in [6, 7, 8]:
   print(month, '月是夏季')
elif month == 9 or month == 10 or month == 11:
   print(month, '月是秋天')
elif month in [12, 1, 2]:
   print(month, '月是冬季')   

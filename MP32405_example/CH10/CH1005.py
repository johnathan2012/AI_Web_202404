# 使用strftime()方法，配合時間格式化字元
from time import strftime, localtime

# 取得當地時間
special = localtime()

d1 = strftime('%Y-%m-%d %H:%M:%S', special)
print('目前日期，時間', d1)

print(strftime('%A, 第%j天', special))

d2 = strftime('%x', localtime())
print('日期', d2)

tm = strftime('%X %p', localtime())
print('時間', tm)

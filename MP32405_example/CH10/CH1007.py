from datetime import *

#計算當前日期到父親節還有幾天？
td = date.today()
fatherDay = date(td.year, 8, 8)
result = fatherDay - td

print('到父親節還有', result)
print('到父親節還有{:4d}天'.format(result.days))

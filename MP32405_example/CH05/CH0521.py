# %運算子處理浮點數

import math # 匯入math模組

#將輸出格式字串存放在變數裡
fmt = '含有4位小數：%.4f'
print('PI', fmt %(math.pi))

radius = (math.pi)*5**2
print('圓面積:', radius)
print('圓面積', fmt % radius)

print('以4位整數輸出 -- %04d' % radius)

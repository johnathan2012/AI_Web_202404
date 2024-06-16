from collections import OrderedDict # 滙入模組

dt = {'A':1, 'B':2, 'C':3, 'D':4}   # 無序字典
odt = OrderedDict(dt)               # 轉換為有序字典
odt['E'] = 5    # 新增一個項目
print(odt)

odt.move_to_end('A') # key A移向最後
print('Key A是最後一個項目')
print(odt)

odt.move_to_end('E', last = False) # key E移向最前
print('Key E是第一個項目')
print(odt)

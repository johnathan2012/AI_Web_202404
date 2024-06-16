import math
# %運算子--格式字串

word = 'Python'
print('I love %s'%word)   #輸出「I love Python」
print('%s was conceived in the late %ds'%(word, 1980))
# 輸出「Python was conceived in the late 1980s」

print('%06d' % 25)

print('PI =', math.pi)
print('PI = %.4f' % math.pi)

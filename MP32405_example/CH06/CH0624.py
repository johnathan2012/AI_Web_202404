matr = [ #3*4二維List
     [11, 12, 13, 14],
     [22, 24, 26, 28],
     [33, 35, 37, 29]]

#雙層for讀取matr
print('一般巢狀for')
for one in matr: # 第一層for廻圈   
   for two in one:  # 第二層for廻圈
      print(two, end = ' ')
   print()

# List Comprehensions
print('以列為主')
print('\n'.join(['{}'.format(one) for one in matr]))

#先讀欄索引 11,22, 33
print('列、欄置換：')
print('\n'.join([''.join(['{0:3d}'.format(row[item])
    for row in matr]) for item in range(4)]))

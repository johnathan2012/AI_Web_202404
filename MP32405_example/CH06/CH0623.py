array = [] # 建立空白矩陣

numRows, numCols = eval(input('輸入列、欄數，按逗點隔開：'))

element = 0 # 存放List元素
for row in range(numRows):
   array.append([]) # 新增List元素
   for column in range(numCols):
      element = eval(input('輸入數值，按Enter鍵：'))
      array[row].append(element)
   print()

sym = '-----' * numCols
print('%5s'%'' , end = '|')
for ct in range(numCols):
    print(f'{ct:^4d}', end = '|')
print('\n-----', sym)

#讀取串列元素
for idx, one in enumerate(array): # 第一層for廻圈
   print('列 ', idx, end = '|')
   for two in one:  # 第二層for廻圈
      #print(format(two, '^5d'), end = '|')
      print(f'{two:^4d}', end = '|') 
   print()   #換行

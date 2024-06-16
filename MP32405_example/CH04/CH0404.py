# 巢狀for產生星形圖

# 雙層 for/in，星形遞增
for one in range(1, 10):
   # 第二層 for/in
   for two in range(0, one):
      print('*', end = '')
   print() #換行

# 雙層 for/in，星形遞減
for one in range(1, 10):   
   # 第二層 for/in
   for two in range(one, 10):
      print('*', end = '')
   print() #換行

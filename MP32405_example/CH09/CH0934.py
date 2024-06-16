#定義函式 total = 0 
def allNums(total):
   
   def oneFun(item, step):

      nonlocal total   # 未加 nonlocal，程式會有異常
      
      print('數值:', end = '')
      for item in range(1, item + 1, step):
         print(f'{item:3d}', end = '')
         total += item
      print()
      return total   # 回傳加總結果
   return oneFun     # 回傳函式物件

# 呼叫函式 allNums
star = allNums(0) #total = 0

# 呼叫函式oneFun，star配合range(1, 20, 3)函式做加總
print('合計:', star(20, 3))

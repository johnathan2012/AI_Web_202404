# 使用global為全域

fruit = 'Orange' # global變數

def Demo():   # 定義函式
   global fruit
   print('最愛水果', fruit)

   fruit = 'Watermelon' # 區域變數
   print('夏天水果', fruit)

Demo() # 呼叫函式

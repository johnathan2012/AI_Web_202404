#使用try/except敘述捕捉索引超出界限值

number = 25, 67, 12, 64   # Tuple

def getIndex(index):      # 定義函式

   #try/except敘述
   try:    
      return (number[index])

   except IndexError as ex:  
      print("錯誤: {0}".format(ex))
      #print('Index', arg)

x = 0
x = int(input('輸入索引回傳元素：'))
print('Tuple Element:', getIndex(x))

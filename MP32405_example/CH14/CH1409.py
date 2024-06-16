# readline()方法讀取檔案

show = ''

with open('../Demo/demo1408.txt', 'rt') as foin:
   
   print('檔案指標：')
    
   while True:
      print(foin.tell(), end = ' ')
      line = foin.readline()
      #print(line, end = '')
      if not line:
         break
      show += line

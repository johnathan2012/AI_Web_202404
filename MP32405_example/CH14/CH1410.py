# 使用 readlines()方法讀取一行並回傳一行

# open()函式，參數'rt'表示讀取文字檔案
with open('../Demo/demo1408.txt', 'rt') as foin:
   total = foin.readlines()
    
#取得行數，再以for廻圈讀取
print('行數：', len(total))
for line in total:
   print(line, end = '')

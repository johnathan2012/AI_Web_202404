# read()方法讀取檔案
show = ''

#每次欲讀取的字元數
capacity = 80
# open()函式，參數'rt'表示讀取文字檔案
with open('../Demo/demo1408.txt', 'rt') as foin:
   while True:
      #讀取80個字元
      segment = foin.read(capacity)

      #顯示內容於螢幕
      #print(segment, sep = '', end = '')
      print(segment)
      #print(segment)
      if not segment:
         break
      show += segment
print('字元數：', len(show))

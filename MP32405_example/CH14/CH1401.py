#使用io模組的StringIO類別 -- 將現有字串以類檔案物件來處理
from io import StringIO

flo = StringIO('Though leaves are many,' +
              '\nthe root is one;' +
              '\nThrough all the lying days of my youth!')

print('讀取17個字元:', flo.read(17))
print('第一行未讀取:', flo.read())

#從the root ...讀起
while True:
    msg = flo.readline()#讀取整行
    if msg == '':
        break
    print(msg.strip())


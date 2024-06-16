# 建立字典

# 使用大括號{}
print('字典物件：\n',
      {'Jan':1, 'Feb':2, 'Mar':3})

#使用zip()函式
weeks = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
         'Thursday', 'Friday', 'Saturday']
title = ['星期天', '星期一', '星期二', '星期三', 
             '星期四', '星期五', '週末']

# 使用zip()函式來組合
wkcomb = dict(zip(title, weeks))
for key in wkcomb:   #讀取字典
    print(f'{key:3s} {wkcomb[key]:10s}')

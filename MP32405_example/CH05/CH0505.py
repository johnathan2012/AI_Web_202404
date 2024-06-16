# for廻圈讀取字串，加入enumerate()函式形成索引

word = 'Programming'
print('index char')
for index, item in enumerate(word):
   # ^5, 欄寬為5, 字元置中對齊
    print(f'{index:^5} {item:^3}')

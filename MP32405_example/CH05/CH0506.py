word = 'They make a hourly wage'
print('字串長度:', len(word))

#表示依字串長度，從索引值0開始，間隔3來取字元
for item in range(0, len(word), 3):
    print(word[item], end = '')

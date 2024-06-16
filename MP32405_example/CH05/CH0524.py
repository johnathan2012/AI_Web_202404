wd = input('輸入欄寬值：')
width = int(wd)
print('=' * width) #依據欄寬值來輸出
score_width = 9 #分數欄寬
name_width = width - score_width #名字欄寬
data = '{0:11s} {1:.2f}'

print('{0:11s} {1}'.format('名字', '分數'))
print('-' * width)
print(data.format('Mary', 68.789))
print(data.format('Tomas', 74.6752))
print(data.format('William', 85))

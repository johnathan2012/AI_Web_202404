# split()方法分割字串

print('split()函式'.center(38, '-'))
wd1 = 'one two three four'
print('原來字串:', wd1)

print('「空白字元」分割字串'.center(34, '*'))
#以預設值空白字元分割字串，list物件回傳
print(wd1.split())

#將字串分割成2+1
print('分割3個字串：', wd1.split(maxsplit = 2))
opr = '--'
opr *= 20
print(opr)

wd2 = 'one,two,three,four'
print('字串二：', wd2)
print('逗點分割字串', end = '->')
print(wd2.split(sep =',', maxsplit = 3))

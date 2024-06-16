pern = [('Mary', 1988, 'Taipei'),
          ('Davie', 1992, 'Kaohsiung'),
          ('Andy', 1999, 'Taichung'),
          ('Monica', 1987, 'Hsinchu'),
          ('Cindy', 1996, 'Taipei')]

#定義sort()方法參數key
st = lambda item: item[0]
pern.sort(key = st)

print('依名字排序：')
for name in pern:
    print('{:6s},{}, {:10s}'.format(*name))

#直接在sort()方法帶入lamdba()函式
pern.sort(key = lambda item: item[2], reverse = True)
print('依出生地遞減排序：')
for name in pern:
    print('{:6s},{}, {:10s}'.format(*name))

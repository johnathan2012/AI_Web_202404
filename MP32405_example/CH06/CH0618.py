#應用一：計算分數平均
score= [(78, 65, 47, 84), (93, 84, 75),
        (65, 88, 91)]

avg = [sum(item)/len(item) for item in score]
print('平均: {0[0]:.3f}, {0[1]:.3f}, {0[2]:.3f}'
      .format(avg))
print()

#應用二：讀取字串長度
fruit = ['lemon', 'apple', 'orange', 'blueberry']

print('%9s'%'字串', '%3s'%'長度')
print('\n'.join( ['%10s:%2d'%(
    item, len(item)) for item in fruit]))
print('*------------------*')

print('%9s'%'字串', '%3s'%'長度')

for item in fruit: #原有的for廻圈讀取
    print(f'{item:>10s}:{len(item):2d}')

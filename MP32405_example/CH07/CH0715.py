from collections import OrderedDict

stud = {'Mary':87, 'Eric':49, 'David':81,
      'Peter':72, 'Judy':67}

#BIF sorted()函式，使用key排序
name = OrderedDict(sorted(
    stud.items(), key = lambda fd: fd[0]))

for key in name:
    print(f'{key:5s} {name[key]}')

print('-' * 20)

#BIF sorted()函式，使用value排序
score = OrderedDict(sorted(stud.items(),
        key = lambda fd: fd[1], reverse = True))
for key in score:
    print(f'{key:5s} {score[key]}')

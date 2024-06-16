# dict()函式產生字典

# (1)配合關鍵字引數
score = dict(John = 87, Eric = 75, Judy = 91, Tomas = 65)
print(score)

# 可迭代者 - Tuple
special = dict([('year', 1988), ('month', 5), ('day', 27)])
print(special)

# 可迭代者 - List
person = dict([['name', 'Mary'], ['sex', 'female']])
print(person)

# 配合zip()函式
week = dict(zip(
   ['Sunday', 'Monday', 'Tuesday'],
   ['週日', '週一', '週二'] ))
print(week)

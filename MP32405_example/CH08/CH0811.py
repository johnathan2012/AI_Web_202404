student = {'Maya': {'Kaohsiung', 'female', 1988},
           'Tomas':{'Taipei', 'male', 1989},
           'Michelle': {'Kaohsiung', 'female', 1990},
           'Steven': {'Taipei', 'male', 1988},
           'Grace': {'Taichung', 'female', 1991} }

# & 運算子
print('女學生', end = '-')
for name, pern in student.items():
    if pern & {'female'}:
        print(name, end = ', ')
print()

print('家住台北，非1988年出生：', end = '')
for name, pern in student.items():
    if 'Taipei' in pern and not pern &{1988}:
        print(name)

#儲存個人的相關訊息
maya = student['Maya']
tomas = student['Tomas']
michelle = student['Michelle']
steven = student['Steven']
grace = student['Grace']

# & - 交集，用方法
print('Maya, Michelle共同點：',
      maya.intersection(michelle))

# | - 聯集
print('Tomas, Steven基本資料\n', tomas | steven)

# ^ 對等差集
print('Maya, grace 城市、出生年份不同\n', maya ^ grace)

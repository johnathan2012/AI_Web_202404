# 字典生成式

score = {'Tom':95, 'Stever':78, 'John':47, 'Eward':67,
         'Cathy':64, 'Eric':52, 'Ivy':72, 'Grac':82,
         'Kevin':93, 'Nacy':35, 'Laura':75, 'David':88}

print('分數大於85\n',
      {k:v for k,v in score.items() if v > 85})

print('分數小於60\n',
      {k:v for k,v in score.items() if v < 60})

#找出分數最低、最高者
min_score = min(zip(score.values(), score.keys()))
print('最低分：', min_score)
max_score = max(zip(score.values(), score.keys()))
print('最高分：', max_score)

# 建立空字典，以分數為key，value以串列存放分數相同者
data = {} #空字典
for key, value in score.items():
    tmp = value // 10 #取整數商數
    if tmp not in data:
        data[tmp] = []
    data[tmp].append(key)

# 讀取字典
for key in data.items():
    #訽問字典裡是否有List
    if isinstance(key, list):
        for value in key:
            print(value)
    else:
        print(key)

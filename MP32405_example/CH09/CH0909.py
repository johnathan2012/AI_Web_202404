# 定義函式
def person(name, sex, city = 'Taipei'):
    return {'name' : name, 'sex' : sex, 'city' : city}

# 呼叫函式
print('基本資料:', person('Judy', 'Female'))
print('基本資料:', person('Steven', 'Male', 'Kaohsiung'))

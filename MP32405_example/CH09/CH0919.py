# 定義函式, 參數使用**運算式
def student(msg, **pern):
    print(msg, '以學生名字排序')
    for key in sorted(pern):
        print(f'{key:8s} {pern[key]}')
    print('-' * 20)

    #使用生成式找出分數低於60
    low60 = {k : v for k, v in pern.items() if v < 60}

    count = len(low60) #取得個數
    print(f'分數低於60, 名單有{count}人')
    print(low60)

#呼叫函式
student('111學年', Mary = 90, Steven = 45,
        Eric = 75, John = 55, Ivy = 75,
        Tomas = 87, Ford = 41, Helen = 88)

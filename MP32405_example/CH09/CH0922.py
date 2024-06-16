# 定義函式
def score(name, n1, n2, n3):
    print(name)
    print('分數:', n1, n2, n3)
    total =  n1 + n2 + n3
    average = total/3
    print(f'總分: {total} 平均:{average:.4f}')

number = [78, 94, 35]

#呼叫函式 -- number串列物件，可迭代
score('Toams', *number)

# 定義函式
def number(n1, n2, n3, n4, n5):
    print('Number:',n1, n2, n3, n4, n5)

#呼叫函式，使用*運算子拆解「可迭代物件」
print('後2個是可迭代物件')
number(11, 12, *range(13, 16))

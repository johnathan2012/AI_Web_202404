# 定義函式
def student(n1, n2, n3, n4, n5,
            One, Two, Three, Four, Five):
    s1 = '分數'; s2 = '總分:'
    re1 = sum(One)
    print('%7s'%n1, s1, One, s2, re1)
    re2 = sum(Two)
    print('%7s'%n2, s1, Two, s2, re2)
    re3 = sum(Three)
    print('%7s'%n3, s1, Three, s2, re3)
    re4 = sum(Four)
    print('%7s'%n4, s1, Four, s2, re4)
    re5 = sum(Five)
    print('%7s'%n5, s1, Five, s2, re5)

# name為串列 score字典物件
name = ['Mary', 'Tomas', 'Francis', 'Judy', 'Rudolf']
score = {'One':(78, 92, 56, 81), 
           'Two': (47, 92, 81, 90),
           'Three': (91, 87, 72, 61),
           'Four': (95, 82, 55, 67),
           'Five':(65, 84, 97, 78)}
# 呼叫函式
student(*name, **score)

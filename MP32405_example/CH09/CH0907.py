# 可變和不可變物件若被修改，對引數傳遞有何影響？

def passFun(name, score):   # 定義函式
    #只有內部的名字被改變
    name = 'Tomas'
    print('名字:', name)
    #新增一個分數，也影響函式之外的串列
    score.append(47)
    print('分數:', score)

na = 'Mary'
sc = [75, 68]
passFun(na, sc)   # 呼叫函式
print(na, '分數', sc)

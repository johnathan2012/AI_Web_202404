# 定義函式, 可變和不可變物件的傳遞

def passFun(name, score):
    print('自訂函式的形式參數')
    print('<name>', id(name))
    print('score >', id(score))

# 呼叫函式
na = 'Mary'; sc = [75, 68]
passFun(na, sc)
print('呼叫函式的實際引數')
print('<na>', id(na))   #不可變物件
print('sc >', id(sc))   #可變物件

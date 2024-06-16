#第一個函式，*score參數接收多個位置引數，sum()函式計算總和
def student(*score):
    return sum(score)

#第二個函式，三個參數，第2個以函式為物件，第3個接收多個引數
def getScore(name, func, *one):
    print(name, '總分:', end = '')
    return func(*one) #回傳函式及參數
    
#呼叫第二個函式
print(getScore('Tomas', student, 78, 65, 92))
print(getScore('Vicky', student,
               95, 74, 45, 84))

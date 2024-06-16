# 定義函式
def stud(name, **dt):
   print('Name:', name)
   print('Score:', dt)

#呼叫函式 - 1個位置引數
stud('Mary')

#呼叫函式 – 1個位置引數，3個關鍵字引數
stud('Tomas', eng = 65, math = 71, chin = 83)

# 第一行輸出「Name: Tomas」
# 第二行輸出「Score: {'math': 71, 'chin': 83, 'eng': 65}」

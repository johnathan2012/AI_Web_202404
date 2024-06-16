# 定義函式
def student(name, *score, StdNo, **pern):
    print('名字:', name, ' 學號:', StdNo,)
    for item in sorted(pern):
         print(f'{item:8s}{pern[item]:<}')
    print('成績：', sorted(score))

#呼叫函式 
student('Tomas', 65, 78, 71, StdNo = '108HJ2501',
        Year = 111, have = '必修', Subject = 'Computer')

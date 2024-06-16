data = {'x':78, 'y':56, 'z':92}   #定義dict

#自訂函式 -- 形式參數的x、y、z來自dict的key
def student(n1, n2, n3, x, y, z): 
    print(f'{n1:>6s}{x:3d}')
    print(f'{n2:>6s}{y:3d}')
    print(f'{n3:>6s}{z:3d}')

# 呼叫函式 -- 第4個實際引數為字典物件，使用**運算子
student('Eric', 'Tom', 'Ivy', **data)

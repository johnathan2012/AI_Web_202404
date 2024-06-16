# 定義函式
def student(n1, n2, n3, x, y, z): 
    print(f' {n1:4s}{x:4d}')
    print(f' {n2:4s}{y:4d}')
    print(f' {n3:4s}{z:4d}')
    print('-'*15)
    print(f' 總分{(x + y + x):4d}')

#定義字典
data = {'x':78, 'y':56, 'z':92}

# 呼叫函式 -- 第3個實際引數為字典物件，前綴**
student('1st', '2nd', '3rd', **data)

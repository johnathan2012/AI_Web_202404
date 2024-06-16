# 修改範例CH0927.py 設區域變數的值

fruit = 'Orange' # global變數

def Demo():   # 定義函式
    fruit = 'Watermelon' # 區域變數
    print('夏天水果', fruit)
    
Demo() # 呼叫函式

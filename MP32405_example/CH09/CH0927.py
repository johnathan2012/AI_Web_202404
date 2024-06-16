# 改變全域變數的值

fruit = 'Orange' # global變數

def Demo():   # 定義函式
    print('最愛的水果', fruit)
    fruit = 'Watermelon' # 改變全域的值
    print('夏天水果', fruit)
    
Demo() # 呼叫函式，發生錯誤UnboundLocalError

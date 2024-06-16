# 函式的參數使用**雙星運算式

def score(**value):   # 定義函式，**收集關鍵字引數
    print('成績', value)

# 呼叫函式
score(eng = 52, comp = 93, math = 62)

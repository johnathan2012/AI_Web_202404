#使用assert敘述

data = [82, 67, 78]   # List

def demo(data):   #定義函式
    total = 0
    for item in data:
        assert item > 60, '輸入的值要大於零'    
        total += item
    return total

print('合計：', demo(data))


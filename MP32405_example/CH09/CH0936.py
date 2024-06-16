# 使用filter()函式

def getNums(n):   # 定義函式
    return n > 2

ary = range(10)   # 產生可迭代物件

# 使用list()將為List物件
print(list(filter(getNums, ary)))

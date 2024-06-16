# all()和any()函式
# num是List，data是Tuple，source是空字典
num = [11, 56]; data = ('one', 'two'); source = {}

print(all(num), all(data), all(source)) # 回傳True, True, True
print(any(data), any(data), any(source)) # 回傳True, True, False

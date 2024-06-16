# 使用filter()函式

ary = range(1, 16) # 數值1~15

# 被3整除者放入result變數
result = list(filter(lambda x : x % 3 == 0, ary))
print(result)

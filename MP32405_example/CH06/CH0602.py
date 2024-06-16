data = 25, 17, 45, 6, 17 # 建立Tuple

print('數值17索引編號：', data.index(17))
# 回傳第2個17的位置
print('第2個17：', data.index(17, 2))

print('以另外方法讀取')
print('data[0:4].index(17)--', data[0:4].index(45))

#print(data.index(17, 2, 4)) # 找不到17，回傳錯誤訊息

data = 258, 12, 37, 69, 47   #Tuple
print('原有內容：', data)

# 預設排序 -- 由小而大
print('由小而大排序：',sorted(data))

# 遞減排序
print('由大而小排序：', sorted(data, reverse = True))
print('data並未改變：', data)

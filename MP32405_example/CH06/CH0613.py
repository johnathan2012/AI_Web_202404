data = 258, 12, 37, 69, 47 #Tuple物件

print('排序前：', data)
print('排序後：', sorted(data)) #排序，由小而大
print('原來資料不變：', data)

ary = list(data)   # 轉成List物件

line = '-'
line *= 35
print(line)

print('轉成串列：', ary)
ary.sort(reverse = True)
convlt = tuple(ary)   # 還原成Tuple物件

print('由大而小排序：', convlt)
print('排序後已改變：', ary)

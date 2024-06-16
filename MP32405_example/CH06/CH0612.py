ary = 12, 178, 34, 92   # Tuple
print('Tuple排序前：', ary)

covlt = list(ary)    # 以list()函式把Tuple轉為List
covlt.sort()         # 呼叫List的sort()
covtp = tuple(covlt) # 以tuple()函式把List再轉回Tuple
print('Tuple排序後的元素：', covtp)

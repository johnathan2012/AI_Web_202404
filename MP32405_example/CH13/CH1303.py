#try/except敘述...as敘述給予Exception型別別名

number = 25, 67, 12 #tuple
try:
    print(number[3])
except Exception as err:

    print(f'錯誤：{err}')

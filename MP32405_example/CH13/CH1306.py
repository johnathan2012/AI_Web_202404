#try/except敘述，except敘述列示多個異常型別

number = 25, 67, 12  # Tuple, index 0~2
try:
    print(number(3)) # 應用中括號[]，卻使用了括號()
except (IndexError, TypeError) as err:
    print('錯誤：', err)


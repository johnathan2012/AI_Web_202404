#try/except敘述，無法捕捉到異常卻引發另一個錯誤

number = 25, 67, 12   # Tuple, index 0~2
try:
   print(number(3)) #應用方括號number[3]，卻使用括號number(3)
except IndexError as err:
   print('錯誤：', err)

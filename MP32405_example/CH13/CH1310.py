# try/exception/finally敘述

def demo(num1, num2):
   try:
      result = divmod(num1, num2)
   except ZeroDivisionError as err:
      print('錯誤', err)
   else:
      print('計算結果', result)
   finally:
      print('完成計算')

one, two = eval(input('請輸入兩個數值，用逗點隔開：'))
demo(one, two)

# try/except/else敘述

num1, num2 = eval(input('請輸入兩個數值，用逗點隔開：'))

try:
   result = num1 / num2

except ZeroDivisionError as err:
   print('Error:', err)

else:
    print('相除結果：', result)

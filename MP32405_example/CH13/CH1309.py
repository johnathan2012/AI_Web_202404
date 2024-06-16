# try/finally敘述

def func(num1, num2):
   try:
      result = num1 // num2
      print('Result:', result)
   finally:        
      print('完成計算')        

func(151, 12) #可得結果
func(1, 0) #引發異常

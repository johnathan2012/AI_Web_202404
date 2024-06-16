# math敘述有多重選擇

mon = int(input('輸入1~12數值取得天數 ->'))

match mon:
   # 使用運算子|(or)組合多個值
   case 1 | 3 | 5 | 7 | 8 | 10 | 12:
      print(mon, '月有31天')
   case 4 | 6 | 9 | 11:
      print(mon, '月有30天')
   case 2:
      print(mon, '月可能是28或29天')
   case _:
      # 輸入數值未在1~12之間
      print('數值不正確')

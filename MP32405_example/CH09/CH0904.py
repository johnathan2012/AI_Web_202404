# (2) 自訂函式有參數，而且函式主體有運算，以return敘述回傳

def total(num1, num2, num3):   # 定義函式，有3個參數值

   result = 0   # 儲存計算結果
   
   for item in range(num1, num2 + 1, num3):
      result += item   # 儲存相加結果

   return result

print('計算數值總和，輸入-1停止計算')

key = input('按y開始，按n停止--> ')

while key == 'y':
    start = int(input('輸入起始值:'))
    finish = int(input('輸入終止值:'))
    step = int(input('輸入間距值:'))
    
    #呼叫自訂函式total
    print(f'數值總和:{total(start, finish, step):,}')

    key = input('按y開始，按n停止-> ')

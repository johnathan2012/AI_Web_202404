# 有參數、回傳值的簡單函式

def bigValue(x, y):   # 定義函式，有兩個參數

   # 找出x, y哪一個值最大
   if x > y:
      result = x
   else:
      result = y

   # 回傳最大值
   return result

num1, num2 = 15, 10

# 呼叫函式，取得函式的回傳值
large = bigValue(num, num2)

print('最大值', large)

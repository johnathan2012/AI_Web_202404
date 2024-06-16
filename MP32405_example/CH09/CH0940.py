#修改範例《CH0929.py》，改用遞廻

def factR(num):
   if num <= 1 : # 0! = 1! = 1
      return 1   # 基本情況，終止遞廻

   # 如果階乘是2(含)以上，自己呼叫本身的函式
   else:
      return (num * factR(num - 1)) #遞廻

print(factR(6))   # 呼叫函式，輸出結果

# Local function

def Outer(num1):   # 函式中有函式
   def Inner(num2):
      return num1 ** num2
   return Inner

# 呼叫函式
result = Outer(5)(3)
print(result)

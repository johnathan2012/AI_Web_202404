# 使用filter()函式

from random import randint

# *data - 將位置引數以tuple收集
def addNum(*data):
   result = 0
   print('index value')
   print('-'*12)
   # 以emumerate()函式回傳index和元素，再以sorted()排序
   for i, j in enumerate(sorted(data)): 
      print(f'{i:^6d}{j:>4d}') 
      result += j
   return result

numbers = [] #空的list

# 隨機產生9個 1~99的數值
for item in range(9):
    numbers.append(randint(1, 99))

outcome = list(filter(lambda n: n % 2 == 0, numbers))
even = tuple(outcome) # 轉為tuple物件

# 呼叫函式 *even將tuple元素拆解傳遞給函式
print('1~99 隨機數')
total = addNum(*even)
print('-'*12)
print('偶數和:', total)

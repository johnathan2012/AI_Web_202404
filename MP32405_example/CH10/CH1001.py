from random import randint, randrange

#產生某個區間的隨機整數
def numRand(x, y):
   cout = 1 #計數器
   while cout <= 10: 
      number = randint(x, y)
      print(number, end = ' ')
      cout += 1
   print()

def numRand2(x, y):
   cout = 1
   result = [] #存放亂數
   while cout <= 10:
      number = randint(x, y)
      result.append(number)
      cout += 1
   return result

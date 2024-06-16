'''
   利用亂數產生1~100之間的數值
'''
import random # 匯入亂數模組
number = random.randint(1, 100) #產生1~100之間的亂數
guess = -1 #儲存猜測數值

#while廻圈
while guess != number:
   guess = int(input('請輸入1~100之間的數字，猜一猜！--> '))

   # if/elif 敘述來反應猜測狀況
   if guess == number:
      print('你猜對了，數字是：', number)
      break
   elif guess >= number:
      print('數字太大了')
   else:
      print('數字太小了')

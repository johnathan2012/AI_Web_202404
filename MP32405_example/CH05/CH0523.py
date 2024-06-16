import math	#匯入math模組

print('PI = {0.pi}'.format(math)) #輸出PI值

print('PI = %10.4f'%(math.pi))	#輸出4位小數
print('PI = {0:010f}'.format(math.pi)) #前方補0欄寬10
radius = (math.pi) * 26 ** 2 #計算圓面積
print('PI = {0:.4f}\n'   #圓面積加千位逗點
      '圓面積 = {1:,.3f}'.format(math.pi, radius)) 

area = int(radius) #轉為整數

print('以十進位、十六進位、二進位輸出：')
print('圓面積 = {0:d}, {0:#x}, {0:#b}'.format(area))
print('靠右 = {0:*>10d}'.format(area)) #*字元填滿
print('置中 = {0:*^10d}'.format(area))

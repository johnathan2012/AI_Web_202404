number = (21, 23, 25, 27 , 29) #Tuple
item = 0 # 計數器，配合tuple的索引值，由0開始

# while廻圈
while item < len(number): # len()函式取得number長度
   print(number[item], end = ' ')
   item += 1 #計數器累加
else:
   print('\n讀取完畢')

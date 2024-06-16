# while廻圈加入計數器

total, count = 0, 2 #儲存加總結果, 設計數器

while count <= 50:  #2,4,6 ~ 50
   total += count #將數值累加
   count += 2
print('2+4+6+...+ 10 累加結果', total) #輸出累加結果

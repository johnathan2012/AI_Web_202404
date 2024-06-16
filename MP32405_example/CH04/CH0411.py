# total儲存總分，score儲存分數, count計數器
total = score = count = 0

# 進入while廻圈，當score為0就結束廻圈
while True:
   score = int(input('輸入分數, 按0結束廻圈：')) #以int()轉為整數
   if score == 0:
      break
   total += score
   count += 1
   
average = float(total / count) # 計算平均值
print('共', count, '科，總分:', total,', 平均:', average)

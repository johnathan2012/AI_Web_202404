# if/elif/else敘述判斷輸入分數

score = int(input('請輸入分數-> '))

if score < 60:
   print(score, '請多多努力！')
elif score < 70:
   print(score, '表現持平！')
elif score < 80:
   print(score, '不錯噢!')
elif score < 90:
   print(score, '好成績!')
else:
   print(score, '非常好！')
    

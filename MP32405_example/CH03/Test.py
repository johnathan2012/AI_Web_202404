# 使用巢狀if
age = int(input('請輸入年齡-> '))

if age >= 6:
   if age >= 15:
      if age >= 18:
         print('所有級別的電影皆可觀賞！')
      else:
         print('可以觀賞輔導級的電影！')
   else:
      print('可以觀賞保護級的電影！')
else:
   print('只能觀賞普通級的電影！')

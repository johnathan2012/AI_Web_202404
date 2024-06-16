#在子類別中呼叫父類別的方法
class Father:       # 基礎類別
   def walking(self):
      print('多走路有益健康!')
        
class Son(Father):  # 衍生類別
   def walking(self):
      Father.walking(self)  # 呼叫父類別的方法
      print('飯後要多多散步')

#產生父類別實體
Steven = Father()
print('Father class')
Steven.walking()
print('Son class')

#產生子類別實體
Joe = Son()
Joe.walking()

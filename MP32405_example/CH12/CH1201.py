# CH12.1 產生繼承
class Father:   # 基底礎類別
   def walking(self):
      print('多走路有益健康!')

class Son(Father):   # 衍生類別Son繼承了父類別Father
   pass

#產生子類別實體
Joe = Son()          # 子類別實體(即物件)
Joe.walking()

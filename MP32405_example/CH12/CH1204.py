#類別的繼承

class Father: #基礎類別一
    def walking(self):
        print('多走路有益健康!')
        
class Mother: #基礎類別二
    def riding(self):
        print('I can ride a bike!')
        
class Son(Father, Mother): #衍生類別
    pass

#產生子類別實體
Joe = Son()
Joe.walking()
Joe.riding()

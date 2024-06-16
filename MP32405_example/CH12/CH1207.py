# 使用內建函式super()呼叫父類別方法

class Mother(): # 父類別
    def display(self, pay):
        self.price = pay
        
        if self.price >= 30000:            
            self.price *= 0.9
        else: self.price
        print(f' = {self.price:,}')        
        
class Son(Mother):          # 子類別
    def display(self, pay): # 覆寫display方法        
        self.price = pay
        super().display(pay)
        
        if self.price >= 30000:            
            self.price *= 0.8
        else:
            self.price        
        print(f'8折 {self.price:,}')
        
Liz = Mother()#基礎類別物件
print('40000 * 9折', end = '')
Liz.display(40000)

Joe = Son()#建立子類別物件
print('35000 * 9折', end = '')
Joe.display(35000)



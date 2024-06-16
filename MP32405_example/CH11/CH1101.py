# 定義類別
class Motor:

    #定義方法一：取得名稱和顏色
    def buildCar(self, name, color):
        self.name = name
        self.color = color

    #定義方法二：輸出名稱和顏色
    def showMessage(self):
        print(f'款式:{self.name:>6s}, \
           顏色:{self.color:4s}')

#物件1，呼叫方法
car1 = Motor()
car1.buildCar('Vios', '極光藍')
car1.showMessage()

car2 = Motor()   # 物件2
car2.buildCar('Altiss', '炫魅紅')
car2.showMessage()

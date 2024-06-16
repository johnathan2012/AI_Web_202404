#利用函式來裝飾類別
def Car(status):   # 裝飾器，以類別來傳入

   class Motor:
      def __init__(self, name):  # 初始化物件
         self.title = name       # 車款
         self.obj = status()     # 取得傳入的實體化物件
         print('車款：', self.title)
            
      def tint(self, opt):       # 取得顏色
         return self.obj.tint(opt)
        
      def power(self, rmp):      # 取得排氣量
            return self.obj.power(rmp)

   return Motor

@Car #裝飾器, Equip = Car(Equip)

class Equip:
   def tint(self, opt):
      match opt:
         case 1: hue = '炫魅紅'
         case 2: hue = '極光藍'
         case 3: hue = '雲河灰'
      return hue
    
   def power(self, rmp):
      if rmp == 4:
         return 1600
      elif rmp == 5: 
         return 1800
        
op1, op2 = eval(input(
    '選擇顏色：1..紅, 2.藍色, 3.灰色 \n' + 
    '排氣量：4.1600, 5.1800...'))

hybrid = Equip('Yaris')
color = '你選擇的顏色：{} '.format(hybrid.tint(op1))
print(color + f'排氣量 {hybrid.power(op2)} c.c')

# 使用類別裝飾器來實作類別的物件

class machine: #以類別為裝飾器

   def __init__(self, func):
      self.func = func
        
   def __call__(self):

      class Motor:

         def __init__(self, obj):
            self.obj = obj
                
         def tint(self, opt):
            return self.obj.tint(opt)
                
         def power(self, rmp):
            return self.obj.power(rmp)
                
      return Motor(self.func())

@machine #裝飾器

class Equip:
   def tint(self, opt):
      match opt:
         case 1: hue = '炫魅紅'
         case 2: hue = '極光藍'
         case 3: hue = '雲河灰'
      return hue
    
   def power(self, rmp):
      if rmp == 5:
         return 1600
      elif rmp == 6: 
         return 1800
    
op1, op2 = eval(input(
    '選擇顏色：1..紅, 2.藍色, 3.灰色 \n' + 
    '排氣量：5.1600, 6.1800...'))

hybrid = Equip()
color = '你選擇的顏色：{} '.format(hybrid.tint(op1))
print(color + f'排氣量 {hybrid.power(op2)} c.c')


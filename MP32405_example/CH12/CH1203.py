#定義類別
class Motor: #基礎類別 或 父類別
    
   '''__init__: 初始化物件
       price, capacity 有預設值，表示是選項參數
       Apollo 售價 65.2 + 1.2 = 66.4，        不含電子鎖
       Hybrid 售價 114.8 + 1.1 + 2.18 = 118.08 含電子鎖
   '''

   def __init__(self, name, price = 65, capacity = 1500): 
      self.name = name           # 車款
      self.price = price         # 定價
      self.capacity = capacity   # 容量

   def equip(self, award):       # 配備加給
      self.price = self.price + award
        
   def __repr__(self):       # 設定輸出格式
      msg = '{0:8s} {1:7.2f} {2:8,}'
      return msg.format(self.name,
            self.price, self.capacity)

class Hybrid(Motor): #衍生類別 或 子類別
        
   def equip(self, award, cell = 2.18):
      Motor.equip(self, award + cell)

   def tinted(self, opr):
      if opr == 1: return '極緻藍'
      elif opr == 2: return '魅力紅'

#建立父類別物件
stand = Motor('standard')

# 設定標頭
print('{:^8s}{:^8s}{:12s}{:5s}'.format(
   '車款', '定價(萬)', '排氣量(c.c)', '配給'))
print('-' * 38)

apollo = Motor('Apollo', price = 65.2, capacity = 1795)    
print(apollo, format('不含電子鎖', '>7s'))    
apollo.equip(1.2) # 配給加價 1.2萬

# 建立子類別物件，但須傳入引數
inno = Hybrid('Innovate', 114.8)
inno.equip(1.1)   # 配給加價 1.2萬
print(f'Hybrid {inno.tinted(2):>20}{"含電子鎖":>5s}')

print()
print(format('三種車款售價', '-^22'))
for item in (stand, apollo, inno):        
   print(item)

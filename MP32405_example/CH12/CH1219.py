from CH1217 import Motor, sportCar, Hybrid

class Vehicle(): #與三個類別無關聯
   def equip(self):
      return 2500

   def show(self):
      return 'Qi無線充電座'

def unite(article):   # 定義函式來輸出各物件
   print(f'{article.show():10s} {article.equip():11,}')

# 設定標頭
print(f'{"品項":^10s}{"售價":^10}')
print('*' * 24)

# 產生範例 <CH1217> 各類別的物件
altiz = Motor('Altiz', 487500)
unite(altiz)
inno = sportCar('Innovate', 638000)
unite(inno)
suv = Hybrid('SUV', 1150000)   # 子類別物件
unite(suv)

car = Vehicle()   # Vehicle 物件
unite(car)

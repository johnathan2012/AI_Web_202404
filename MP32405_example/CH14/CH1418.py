import json

class Motor:
   def __init__(self, name, color, size):
      self.name = name
      self.color = color
      self.size = size
        
# 建立物件
altis = Motor('Altizz', 'Gray', 1795)

# 取得dump()方法中default參數值，自行定義可序列物件
def show(car):
   return{
      'Car'      : car.name,
      'Color'    : car.color,
      'Capacicy' : car.size
   }

altisJn = json.dumps(altis,
        sort_keys = True, default = show)
print('JSON\n', altisJn)

altisP = json.loads(altisJn)
print('dict 物件\n', altisP)


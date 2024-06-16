# 定義函式
class people:

   ''' __str__()讓輸出字串更易閱讀，
      無此方法時，只會輸出
      <__main__.people object at 0x000001AC37A17520>
   '''
   
   def __init__(self, city):   # 物件初始化
      self.city = city

   def __str__(self):   # 覆寫__str__()加入控制格式
      return f'{self.city:-^16}'

# 產生含有引數的物件
addr = people('Kaohsiung')
print(addr)

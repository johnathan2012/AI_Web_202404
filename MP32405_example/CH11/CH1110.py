class Birth():   # 定義函式
   
   def __init__(self, name, y, m, d):   # 初始化      
      self.title = name
      self.year = y    # 年
      self.month = m   # 月
      self.date = d    # 日

   def __str__(self):
      print('Hi!', self.title)
      yr = 'Birth - {}年'.format(str(self.year))
      mo = '{}月'.format(str(self.month))
      return yr + mo + f'{str(self.date)}日'

   def __repr__(self):
      return '{}年 {}月 {}日'.format(
         self.year, self.month, self.date)

#產生物件
p1 = Birth('Grace', 1987, 12, 15)
print(p1)
print(p1.title, 'birth day: ', repr(p1))

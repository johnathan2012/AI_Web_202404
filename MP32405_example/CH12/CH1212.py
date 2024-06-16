#使用property()函式 -- 3

class Student:
   def __init__(self, birth):
      if birth == None:
         raise ValueError('不能是空字串')
      #__birth: 私有屬性
      self.__birth = birth

   def getBirth(self):   # 取得私有屬性__birth
      return self.__birth

   def setBirth(self, birth):   # 設定私有屬性__birth
      self.__birth = birth

   def delBirth(self):
      del self.__birth   # 刪除私有屬性__birth
   birth = property(getBirth, setBirth,
                     delBirth, 'birth 特性說明')

tom = Student('1998/5/21') # 建立物件
print('Tom 生日', tom.birth)
tom.birth = '1998/5/21'

#使用property -- 2, 修改CH1210.py

class Student:
   def __init__(self, birth):
      if birth == None:
         raise ValueError('不能是空字串')
      #__birth: 私有屬性
      self.__birth = birth

   def getBirth(self):
      return self.__birth

   def setBirth(self, birth):
      self.__birth = birth

tom = Student('1998/5/21')
print('Tom 生日', tom.getBirth())
tom.setBirth('1998/5/21')


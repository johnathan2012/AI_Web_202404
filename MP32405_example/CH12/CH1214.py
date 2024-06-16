# 在父類別使用特性
class Student:
   def __init__(self, birth):
      if birth == None:
         raise ValueError('不能是空字串')
      #__birth: 私有屬性
      self.__birth = birth
        
   @property        # getter為birth建立一個特性
   def birth(self):
      return self.__birth
    
   @birth.setter    # 附加 setter 設定器
   def birth(self, value):
      if not isinstance(value, str):
         raise TypeError('應該是字串')
      self.__birth = value
        
   @birth.deleter   # 附加 deleter刪除器
   def birth(self):
        raise AttributeError('屬性不能刪除')   


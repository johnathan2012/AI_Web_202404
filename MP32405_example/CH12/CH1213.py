#使用property()函式 -- 變更為裝飾器

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
    def birth(self, birth):
        self.__birth = birth
        
    @birth.deleter   # 附加 deleter刪除器
    def birth(self):
        del self.__birth    

tom = Student('1998/5/21') # 建立物件
print('Tom 生日', tom.birth)
tom.birth = '1998/5/21'

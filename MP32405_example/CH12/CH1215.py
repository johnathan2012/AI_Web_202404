#繼承的子類別使用特性

from CH1214 import Student

class Person(Student):    
        
    @property #getter為birth建立一個特性
    def birth(self):
        return super().birth
    
    @birth.setter #附加 setter 設定器
    def birth(self, value):
        super(Person, Person).birth.__set__(self, value)
        
    @birth.deleter # 附加 deleter刪除器
    def birth(self):
        super(Person, Person).birth.__delte__(self)    

eric = Person('1998/5/21') # 建立物件
print('Eric 生日', eric.birth)

#使用property

class Student:
    def __init__(self, birth):
        self.birth = birth

tom = Student('1998/5/21')
print('Tom 生日', tom.birth)
 

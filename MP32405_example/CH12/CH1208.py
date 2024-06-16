#__init__()方法呼叫super()

class Parent():      # 父類別
    def __init__(self):
        print('I am parent')
        
class Child(Parent): # 子類別
    def __init__(self, name):
        super().__init__()   # 呼叫父類別__init__()方法
        print(name, 'is child')

tom = Child('Tomas') # 子類別實體


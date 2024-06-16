#繼承的搜尋順序

class Parent(): # 父類別有兩個方法
    def show1(self):
        print("Parent method one")
        
    def show2(self):
        display("Parent method two")
        
class Son(Parent):   # 子類別一
    def display(self):
        print('Son method')
        
class Daughter(Parent):   # 子類別二
    def show2(self):
        print('Daugher method one')
        
    def display(self):
        print('Daughter method two')
        
class Grandchild(Son, Daughter):   # 有兩個父類別
    def message(self):
        print('Grandchild method')
 
eric = Grandchild()   # 子子類別物件
# 先找到自己的方法
eric.message()

# 依順序, Grandchild > Son
eric.display()

# Grandchild > Son > Daughter
eric.show2()

# Grandchild > Son > Daughter > Parent
eric.show1()

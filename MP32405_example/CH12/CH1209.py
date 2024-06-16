# __bases__屬性動態記錄父類別

class Father():   # 父類別一
   def display(self, name):
      self.name = name
      print('Father name is', self.name)
        
class Mother():   # 父類別二
   def display(self, name):
      self.name = name
      print('Mother name is', self.name)
        
#子類別繼承Father, Mother
class Child(Father, Mother):
   pass

class Son(Father): # 子類別繼承Father
   pass

print(Child.__name__, '類別, 繼承兩個基礎類別')
for item in Child.__bases__:
   print(item)

Tom = Son()   # 子類別實體，只有一個父類別
Tom.display('Eric')
print(Son.__name__,'類別，一個父類別')
print(Son.__bases__)
Son.__bases__ = (Mother,)
Tom.display('Judy')

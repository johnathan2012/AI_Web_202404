# 定義類別，Python採動態型別，不同的物件傳入不同型別的資料
class Student:
    def message(self, name): # 方法一
        self.data = name
    def showMessage(self):   # 方法二，輸出物件屬性
        print(self.data)

# 第一個物件，以字串做傳遞
s1 = Student()
s1.message('James McAvoy')   # 呼叫方法時傳入字串
s1.showMessage()

s2 = Student()# 第二個物件
s2.message(78.566)# 呼叫方法時傳入浮點數值
s2.showMessage()

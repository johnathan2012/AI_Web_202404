from datetime import date

#組合的簡易作法
class Student:   # 學生
   def __init__(self, *name):
      self.name = name

class Room:     # 教室
   def __init__(self, title, tday):
      self.title = title
      self.today = tday
      print('上課日期：', self.today)
      print('上課教室：', self.title)

class School:   # 學校
   def __init__(self, student, room):
      self.student = student
      self.room = room

   def display(self):
      print('Student:', self.student.name)

tday = date.today()   # 取得今天日期
eric = Student('Eric', 'Vicky', 'Emily')   # Student物件
abc123 = Room('Abc123', tday)              # 上課教室
tc = School(eric, abc123)                  # School實體
tc.display()#呼叫方法

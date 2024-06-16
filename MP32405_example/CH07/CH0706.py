# pop()方法移除字典項目

def readItem():   # 定義函式讀取字典項目
   for item in student:
      print(f'{item:8s} {student[item]:3d}')

student = {'Tomas' : 95,
           'Vicky' : 89,
           'Michelle' : 87,
           'Peter' : 74,
           'Charles' : 62}

readItem()   # 呼叫函式
del student['Peter']   # del運算子移除key為Peter的項目
student.pop('Tomas')   # pop()方法移除key為Tomas的項目
print('移除兩個項目')    # popitem()方法移除最後一個項目
readItem()

student.popitem()
print('移除最後一個項目')
readItem()

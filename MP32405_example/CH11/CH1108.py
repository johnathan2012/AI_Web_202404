class Student:   # 定義類別
    def score(self, s1, s2, s3):   # 成員方法
        return (s1 + s2 + s3) / 3

Tomas = Student() # 物件
print(Tomas.score(92, 83, 62))   # 輸出79.0

Tomas.subject = []   # 自訂屬性
Tomas.subject.append('math')
print(Tomas.subject)   # 輸出['math']

Tomas.birth = '2003/9/12'
Tomas.subject[0] = 72
print(Tomas.__dict__)
print(Tomas.__class__)

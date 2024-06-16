class Student:   # 定義類別
    def score(self, s1, s2, s3):   # 成員方法
        return (s1 + s2 + s3) / 3

Tomas = Student() # 物件
print(Tomas.score(92, 83, 62))   # 輸出79.0

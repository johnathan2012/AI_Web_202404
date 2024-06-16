# 建立一個儲存名稱和各科成績的二維List
student = [['Mary', 55, 68, 74],
	   ['Tomas', 77, 95, 88],
	   ['Eric', 68, 91, 72]]

# 利用Unpacking拆解每列的名稱和各科分數給不同變數儲存
for(name, math, english, computer) in student:
    print('%6s'%name, '總分:',
        (math + english + computer))

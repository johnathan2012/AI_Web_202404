#定義函式，有5個形式參數，
def total(name, n1, n2, n3, n4):
	result = 0 #result區域變數
	result = sum(price)   #sum內建範圍
	print(name, '$', result)

#建立可迭代物件 -- 序列物件
price = [78, 92, 65, 55]   # price全域變數
total('早餐', *price)

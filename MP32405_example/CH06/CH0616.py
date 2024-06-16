# 修改範例CH0615.py，以生成式表達會更簡潔

numB = [] #空的List
numB = [item for item in range(10, 50)if(item % 9 == 0)]
print('10~50被9整除之數：', numB)

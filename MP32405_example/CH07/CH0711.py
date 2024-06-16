from collections import defaultdict # 匯入模組

df = defaultdict(int)   # 以int為參數

df['One']; df['Two']    # key不存在
df['Three'] = 3         # 設不存在key, value = 3

print(df) 

print('List', list(df))   # 輸出key

print('Tuple', tuple(df))

print(dict(df))  # 變成字典

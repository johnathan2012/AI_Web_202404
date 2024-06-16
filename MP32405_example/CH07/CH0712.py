from collections import defaultdict # 匯入模組

wd = 'initially'
df = defaultdict(int)   # 以int()函式為它的參數

# 讀取字串並統計相同key的次數
for key in wd:
    df[key] += 1
    
# 轉成List
print(list(df.items()))

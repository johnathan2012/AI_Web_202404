# 使用[]運算子取得字典的key, value

# 產生字典
score = {'John' : 85, 'Eric' : 47,
    'Judy' : 85, 'Tomas' : 74, 'Hank' : 81}

# 使用[]運算子，依key取value
print(f"成績 Eric {score['Eric']}, John {score['John']}")

# 使用[]運算子，依key變更value
score['Tomas'] = 86

# 使用[]運算子，新增字典項目
score['David'] = 92
score['Monica'] = 63

# 讀取字典項目
for k in score:
   print(f'{k:6s}-> {score[k]}')

print(iter(score))#無法顯示結果
print(list(iter(score)))   # 輸出key

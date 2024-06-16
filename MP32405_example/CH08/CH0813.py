# 集合生成式

word = 'initiative'

# 統計字元，加速資料的讀取
target = {single : word.count(single) for single in set(word)}
print('字元:', target)

# 統計字元，只顯示重複性高
target = {single : word.count(single) for single in set(word)
          if word.count(single) > 1}
print('字元:', target)

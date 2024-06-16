# count()統計字元出現次數

sentence = '有個身材嬌小的女孩在瑞士一處小村莊裡誕生'
num = sentence.count('小')
print('小 出現', num, '次')
# 方法count()指定範圍
word = 'when he crosses the Atlantic by steamship'
print(f"s 出現 {word.count('s', 0, 15)}次")

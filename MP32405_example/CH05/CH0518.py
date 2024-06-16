# 字串的大小寫相關方法
word = 'HELLO WORLD PYTHON'
print('原來字串：', word)
print('第一個字詞的首字元是大寫', word.capitalize())
print('單字字首是大寫', word.title())     # 單字開頭首字元會大寫
print('全部轉為小寫字元', word.lower())   # 轉為小寫
print('是否只有字首為大寫字元', word.istitle())
print('是否皆為大寫字元', word.isupper())
print('是否皆為小寫字元', word.islower())

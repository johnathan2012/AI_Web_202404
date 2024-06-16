# 使用三元運算子X if C else Y
#依據接收的字母來產生不同的問候語

gender = input('請以M或F表示性別-> ')

# or運算子接收大寫M或小寫m的字母
print('帥哥，你好!' if gender == 'M' or
      gender == 'm' else '美女，日安！')

# find()方法搜尋字串的位置
word = '''We all look forward
   to the annual ball  
   because
   it’s great time to dress up.'''
print(word)
print('all 索引:', word.find('all')) #尋找all子字串，從索引編號0開始
print('all 索引:', word.find('all', 7))#尋找子字串all，從索引编號7開始


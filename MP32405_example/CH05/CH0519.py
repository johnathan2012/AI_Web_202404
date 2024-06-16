# 字串對齊的相關方法
word = 'Happy'

print('原字串', word)
print('字串置中，* 填補', word.center(11, '*'))
print('欄寬10，字串靠左', word.ljust(10, '-'))
print('欄寬10，字串靠右', word.rjust(10, '#'))

number = '1234'
print('字串左側補0:', number.zfill(6))
numOne = '11\t12\t13'
print('原字串', numOne)
print('Tab鍵轉4個空白字元:', numOne.expandtabs(4))

word2 = 'Hello,Python'
print('以逗點分割字元', word2.partition(','))
word3 = 'One\nTwo\nThree'
print('依\\n分割字串', word3.splitlines(True))

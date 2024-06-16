#參考範例《CH0433D.py》
msg = 'Raise your hand if you are overly tired'
frequency = 0      # 統計字元數
for word in msg:   # 讀取字串
   if word == 'a': # 統計字元a出現次數
      frequency += 1
print(frequency, '次')

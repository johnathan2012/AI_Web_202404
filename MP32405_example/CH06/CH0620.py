num = ['AB01', 'AB425', 'CH004', 'CK4131',
       'DD0048', 'Dy00231']
room = ['A', 'B', 'C']
rooms = [r + '-' + n for r in room for n in num
    if r[0] == n[0]]

for item in rooms:   # 讀取生成式符合條件者
   print(item)

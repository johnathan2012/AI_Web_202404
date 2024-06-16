wd1 = ['2022'] # List - year
wd2 = ['Jan', 'Feb', 'Mar'] # List - month

# List Comprehensions
print('List Comprehensions\n',
      [(y, m) for y in wd1 for m in wd2 ])

# double for/in
combin = [] #List
for y in wd1:
     for m in wd2:
         combin.append((y, m))
print('雙層for/in讀取：\n', combin)

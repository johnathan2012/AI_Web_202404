# 年息, 存款額
rate, money = 3.0, 50000
target = 2 * money   # 獲利目標
year = 0  # 年份

# 當存款額 < 獲利目標
while money < target :
   year += 1
   interest = money * rate / 100   # 計算利息
   money += interest               # 本金+利息
   #print(f'第{year}年, 存款額 = {money}')

print(f'第{year}年，存款額翻倍')

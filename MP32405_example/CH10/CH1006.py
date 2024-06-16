import time

special = '2022-04-22 07:48:06'
target = time.strptime(special, '%Y-%m-%d %H:%M:%S')
print(target) # 以時間結構回傳


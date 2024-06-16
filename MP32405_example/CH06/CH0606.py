score = [78, 56, 93] #list
eng, chin, mat = score #Unpacking
print(f'分數:{eng:3d},{chin:3d},{mat:3d}')

x = 'Mary'; y = '1995/4/3'; z = 165
ary2 = (x, y, z) #Packing
name, birth, tall = ary2 #Unpacking
print(f'名字：{name:>4s}')
print(f'生日：{birth:9s}, 身高：{tall}')

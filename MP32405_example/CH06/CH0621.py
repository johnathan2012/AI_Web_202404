#應用：將兩個串列組合
result = []
area = ['北', '南']
city = ['左營', '楠梓', '鳳山']
for one in area:
    if one != '南':
        for two in city:
            if two != '鳳山':
                result.append(one + two)
print('高雄北區:', result)
comb = [itA + itB for itA in area for itB in city
         if(itA == '南' and itB == '鳳山')]
print('高雄南區:', comb)

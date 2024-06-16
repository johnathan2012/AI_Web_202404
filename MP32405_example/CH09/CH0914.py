# 使用「*星號運算式」(start expression)

pern = ('David', 'Male', 95, 68, 72)    #Tuple

name, sex, *score = pern    # Tuple拆解用法
print(name)    #  輸出'David'
print(score)   #輸出[95, 68, 72]

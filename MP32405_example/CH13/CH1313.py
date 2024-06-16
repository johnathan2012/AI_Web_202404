# 在try/except敘述使用 raise敘述
def demo(data, num):    
    try:        
        data[num]
        
    except IndexError as err:
        print(err)
        raise IndexError('索引超出界值')
    
    else:
        print(data[num])

ary = ['Tom', 'Vicky', 'Steven']#List
demo(ary, 1)
demo(ary, 3)

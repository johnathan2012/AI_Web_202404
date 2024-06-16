
try:
    print(1 / 0)
except Exception as err:
    raise TypeError('錯誤') from err
'''

def demo(*value):
    value = []
    if value == 0:
        raise ZeroDivisionError('n 為 零')
    else:
        print(n)
try:
    demo(0)

except ZeroDivisionError as err:
    print(err)
'''

#try/except敘述，使用sys.exc_info()

import sys

number = 25, 67, 12   # Tuple, index 0~2

try:
    print(number[3]) # 應用中括號[]，卻誤用括號()

except IndexError as err:
    print('錯誤：', err)

except: #可攔截取所有異常，放在所有except敘述的最後
    print('錯誤：{0[0]}\n {0[1]}\n {0[2]}'.format(
        sys.exc_info()))
    

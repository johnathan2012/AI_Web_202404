# try/except 配合 raise敘述

try:
    raise Exception('引發錯誤')

except Exception as err:
    print(err)
else:
    print('沒有錯誤')

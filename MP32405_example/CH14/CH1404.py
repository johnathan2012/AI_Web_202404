# 以內建函式print()編寫檔案

prose = '''
I made my song a coat
Covered with embroideries '''

# wt - 覆寫舊有資料
fo = open('D:\\PyCode\\Demo\\demo1404.txt', 'wt')
print(prose, file = fo, sep = '', end = '')
fo.close()   # 關閉檔案，緩衝區的資料才會輸出

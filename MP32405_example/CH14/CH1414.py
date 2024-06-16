#以特殊字元才能有編碼、解碼作用
wd = 't\u00f4t'
#二進位編碼
wdb = wd.encode('utf-8')
#進行解碼
print(wdb.decode('utf-8'))

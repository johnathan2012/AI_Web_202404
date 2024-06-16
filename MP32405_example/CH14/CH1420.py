#藉助'\u2605'說明編碼
word = 'Holiday'
word = '\uFFA0'
print('Length:', len(word))#字串長度

#將unicode字元編碼成bytes
bed = word.encode('utf-8')
print('Bytes:', bed)

#utf-8編碼可改變字串長度
print('長度改變：', len(bed))
print('edb type:', type(bed))

#解碼 -- decode()方法, 不會以Holiday還原
dedb = bed.decode('utf-8')
print('Decoding:', dedb)
type(dedb)

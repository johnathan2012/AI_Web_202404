#內建函式open()開啟檔案，write()寫文字檔

yeats = '''
Where the wandering water gushes

From the hills above Glen-Car,

In pools among the rushes

That scarce could bathe a star,

We seek for slumbering trout

Give them uniquiet dream;
'''

#建立新檔，以文字模式寫入
fn = open('../Demodemo1403.txt', 'wt')
fn.write(yeats)#將字串寫入檔案
fn.close()#關閉檔案

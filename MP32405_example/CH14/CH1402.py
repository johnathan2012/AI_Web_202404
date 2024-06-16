# open()方法的 mode -- 'w+'清空檔案內容

fo = open('../Demo/demo1402.txt', 'w+')    
show = 'Though leaves are many\n'
print('字串長度：', len(show))

fo.write(show)
print('文件目前位置：', fo.tell())

#從檔案開頭，移動3個字元
fo.seek(3, 0)
print('文件目前位置：', fo.tell())
fo.close()

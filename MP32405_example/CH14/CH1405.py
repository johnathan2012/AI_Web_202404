# 以內建函式write()分段寫入檔案 -- 切片作法

prose = '''
To his Heart, bidding it have no Fear
Be you still, be you still, trembling heart;
Remember the wisdom out of the old days:
Him who trembles before the flame and the flood,
And the winds that blow through the starry ways,
Let the starry winds and the flame and the flood
Cover over and hide, for he has no part
With the lonely, majestical multitude.
Covered with embroideries'''

fo = open('../Demo/demo1405.txt', 'wt')
amount = len(prose)   # 取得字串數
separate, mass = 0, 200

# prose[start: end]做切片
while True:
    if separate > amount:
        break
    fo.write(prose[separate : separate + mass])    
    separate += mass
fo.close()

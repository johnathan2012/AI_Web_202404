import copy # 滙入copy模組，做深層複製

ary = [11, [22, 44], 33, 36, 39] # List中有List
target = copy.deepcopy(ary)  # 複製
print(f'ary {ary}\ntarget {target}')


target[-1] = 172   # 變更最後一個元素
print('改變target最後一個元素')
print(ary, '\n', target)

ary[1][1] = 88
print('改變ary第2列、第2欄元素')
print(ary, '\n', target)

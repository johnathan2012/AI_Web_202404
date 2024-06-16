# 集合生成式

fruit = ['Banana', 'Apple', 'Morello',
         'Strawberry', 'Pineapple']   # List
# 產生集合生成式
num = {len(item) for item in fruit}
print('字串長度', num)

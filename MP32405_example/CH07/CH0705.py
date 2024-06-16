# 判斷字典是否有某個項目

score = {11:'Mary', 12:'John', 13:'Andy', 14:'Bob'}

print('字典:'); print(score)
print('Score長度：', len(score)) #回傳字典長度

del score[14] #刪除score[14]
print('刪除key 14'); print(score)

print('Key 12 Score?', 12 in score)
print('Key 14 Score?', 14 not in score)

#使用for廻圈讀取key輸出對應的value
for key in iter(score):
    print(f'{key:2d}, {score[key]:4s}')

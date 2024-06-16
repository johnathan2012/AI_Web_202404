#定義函式
def student(name, *score, subject = 4):
    if subject >= 1:
        print('名字：', name)
        print('共有', subject, '科, 分數：', *score)
    total = sum(score) #合計分數
    print(f'總分：{total}, 平均:{total/subject:.4f}')

#呼叫函式
student('Peter', 78, 65, 93, 81)
student('Wanda', 65, 90, 57, subject = 3)

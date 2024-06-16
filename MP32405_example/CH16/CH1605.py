import turtle   # 匯入海龜模組

turtle.setup(250, 200)        # 產生250 X 200畫布
turtle.bgcolor('LightGray')   # 背景為淺灰色

show = turtle.Turtle()        # 建立畫布物件
show.pen(pensize = 7, pencolor = 'Gray', fillcolor = 'White')

show.speed(1)                 # 畫筆速度為慢

# 畫一個簡單三角形並上色
show.begin_fill()     # 開始上色
for item in range(3):
   show.fd(80)        # 前進70像素
   show.left(120)     # 畫筆右轉90度
show.end_fill()       # 結束上色

show.circle(45, 360, 3) # 繪製三角形

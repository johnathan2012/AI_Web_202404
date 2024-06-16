import turtle   # 匯入海龜模組

turtle.setup(250, 200)        # 產生250 X 200畫布
turtle.bgcolor('Gainsboro')   # 背景為淺灰色

show = turtle.Turtle()        # 建立畫布物件

show.color('White', 'Gray')   # 畫筆為白色

show.pensize(5)               # 畫筆大小
show.speed(1)                 # 畫筆速度為慢

# 畫一個簡單矩形並上色
show.begin_fill()     # 開始上色
for item in range(4):
   show.fd(70)        # 前進70像素
   show.right(90)     # 畫筆右轉90度
show.end_fill()       # 結束上色

show.pen(pensize = 10, pencolor = 'Gray')
show.circle(40, 360, 4) # 繪製菱形

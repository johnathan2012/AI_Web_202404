import turtle   # 匯入海龜模組

turtle.setup(250, 200)       # 產生250 X 200畫布
turtle.bgcolor('Gray')       # 背景為灰色

show = turtle.Turtle()       # 建立畫布物件
turtle.colormode(255)        # 變更色彩以數值表示
show.pencolor(255, 255, 255) # 畫筆為白色
show.pensize(10)             # 畫筆大小
show.speed(1)                # 畫筆速度為慢

show.penup()                 # 畫筆懸空
show.goto(-60, 0)            # 移向指定座標
show.pendown()               # 放下畫筆
show.left(80)                # 左轉90度
show.goto(0, 60)
show.right(130)              # 右轉130度
             
show.fd(100)                 # forward()方法簡寫，前進100像素
show.right(130)              # 畫筆右轉130度
show.goto(-60, 0)

import turtle            # 匯入海龜模組

turtle.setup(200, 200)   # 產生200 X 200畫布
turtle.speed(1)          # 把畫筆速度變慢
turtle.goto(-50, 50)     # 設定x、y座標為(-50, 50)
turtle.goto(50, 50)
turtle.goto(-50, -50)
turtle.goto(50, -50)
turtle.home()   # 回到原點(0, 0)同turtle.goto(0, 0)

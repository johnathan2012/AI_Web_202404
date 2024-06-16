import turtle   # 匯入海龜模組

turtle.setup(350, 300)        # 產生350 X 300畫布
turtle.bgcolor('Gray21')      # 背景為灰色

show = turtle.Turtle()        # 建立畫布物件
show.pensize(2)               # 畫筆大小
show.speed(0)                 # 畫筆速度為慢

colors = ['Red', 'Magenta', 'Blue', 'Cyan',
          'Green', 'Yellow', 'Pink']
for item in range(len(colors)):   # 產生色環
   for tint in colors:  # 產生圓環依序給予顏色
      show.color(tint)  # 顯示顏色
      show.circle(75)   # 產生半徑75的色環
      show.left(10)     # 左轉10度
show.hideturtle()       # 隱藏畫筆

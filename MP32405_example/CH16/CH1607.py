import turtle   # 匯入海龜模組

turtle.setup(300, 300)    # 產生300 X 300畫布

show = turtle.Turtle()    # 建立畫布物件
show.pencolor('Gray21')   # 畫筆為灰色
show.pensize(1)           # 畫筆大小

# 畫一個螺旋圖
for item in range(100):
   show.fd(item * 5)  # 依值前進   
   show.right(121)    # 畫筆右轉121度
   
turtle.mainloop()     # 開始主事件的循環

# 繪製能旋轉的太極
from turtle import *
import time

setup(500, 500)

# 定義函式，畫筆上色繪製弧形
def penPaint(tint, rd, degree):
   color(tint)   # 右側黑色半圓
   begin_fill()  # 畫筆開始上色
   circle(rd, degree)   # 依半徑值, 180度繪製半圓弧線
   end_fill()    # 畫筆結束上色

# 定義函式，移動畫筆到指定位置
def penMove(angle1, angle2, num):
   penup()   
   right(angle1)
   fd(num)
   left(angle2)
   pendown()


# 定義函式，繪製太極
def Taichi():
   speed(10)
   #pensize(1)

   penPaint('Gray', 240, 180)     # 右側黑色大半圓
   penPaint('Snow', 240, 180)     # 左側白色大半圓
   penPaint('Gray', 120, -180)    # 下方黑色小半圓
   penPaint('Snow', -120, -180)   # 上方白色小半圓

   penMove(90, 90, 160)
   penPaint('DarkGray', 40, None) # 繪製上方的黑色小圓
   penMove(90, 90, 240)
   penPaint('Snow', 40, None)     # 繪製下方的白色小圓

# 定義函式，產生可以向右轉案的圖案
def spin(dg):
   penup()  # 抬起畫筆
   home()   # 畫筆回到原點(0, 0)
   right(90 + dg * num)  # 畫筆依角度向右轉
   fd(240)  # 畫筆前進240像素
   left(90) # 畫筆左轉90度
   Taichi() # 呼叫函式，繪製太極圖案

# 移動畫筆到指定座標
penup()
goto(0, -240)
pendown()

Taichi()         # 呼叫函式，繪製太極圖案
hideturtle()     # 隱藏畫筆
   
num = 0

try:
   while True:
      tracer(0)   # 不斷地更新螢幕的動畫
      clear()     # 清除turtle的繪圖
      spin(5)     # 呼叫函式，轉動圖案，值愈大，轉動愈快
      num += 1
      update()    # 產生動畫後，持續更新螢幕
      time.sleep(0.01)      
except:
   print('Exit')

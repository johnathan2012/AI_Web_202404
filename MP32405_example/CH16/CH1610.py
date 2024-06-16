# PIL 開啟圖檔，取得圖檔的基本訊息
from PIL import Image

file = '../Demo/Pict/puppet02.png'  # 圖檔路徑

with Image.open(file) as photo:
   left, upper, right, lower = photo.getbbox()
   print(f'Left = {left}\nUpper = {upper}')
   print(f'Right = {right}\nLower = {lower}')

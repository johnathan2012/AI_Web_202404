# PIL 開啟圖檔，取得圖檔的基本訊息
from PIL import Image

file = '../Demo/Pict/puppet02.png'  # 圖檔路徑

with Image.open(file) as photo:
   # 屬性size取得圖片的寬、高
   width, height = photo.size
   print(f'{width} X {height}')

   # 屬性format獲取圖片格式
   print('圖檔格式', photo.format)

   # 屬性mode取得圖片色譜
   print('模式', photo.mode)

   # 以字典回傳圖片訊息
   imgData = photo.info
   for k, v in imgData.items():
      print(k, v)
   # 取得圖片單一色譜的最小和最大像素
   print(photo.getextrema())
   print('色譜', photo.getbands())
   photo.show()   # 顯示圖片

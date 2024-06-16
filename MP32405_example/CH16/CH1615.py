# rotate()方法旋轉圖片
from PIL import Image

# 圖檔路徑
file = '../Demo/Pict/ylotus.png'

# 開啟圖檔，with/as於執行後自動釋放資源
with Image.open(file) as photo:
   img = photo.rotate(45, expand = True,
      resample = Image.Resampling.BILINEAR)
   img.save('../Demo/Pict/R45E.png')

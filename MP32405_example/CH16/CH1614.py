# rotate()方法旋轉圖片，角度負值是順時針旋轉
from PIL import Image

file = '../Demo/Pict/lotus.jpg'  # 圖檔路徑

# 開啟jpg格式圖檔，with/as於執行後自動釋放資源
with Image.open(file) as photo:
   img = photo.rotate(-135).save(
      '../Demo/Pict/lotusR135.jpg')

file2 = '../Demo/Pict/lotusR135.jpg'
with Image.open(file2) as photo:
   photo.show()

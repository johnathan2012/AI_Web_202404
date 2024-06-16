# PIL 開啟圖檔，resize()方法重設圖片的大小
from PIL import Image

file = '../Demo/Pict/puppet02.png'  # 圖檔路徑

# 開啟圖檔，重設大小並另存另一個檔案
with Image.open(file) as photo:
   width, height = photo.size   # 取得原有圖片大小
   # 方法resize()依width, height重設圖片的大小
   newPng = photo.resize((width // 2, height // 2))
   # 依指定路徑另存新的檔案
   newPng.save('../Demo/Pict/1612.png')
   photo.show()   # 顯示圖片

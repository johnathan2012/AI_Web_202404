# transpose()方法翻轉圖片
from PIL import Image

# 圖檔路徑
file = '../Demo/Pict/puppet02.png'

# 開啟圖檔，
with Image.open(file) as photo:
   img = photo.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
   #img = photo.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
   img.save('../Demo/Pict/trans.png')

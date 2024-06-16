from PIL import Image, ImageFilter

# 圖檔路徑
file = '../Demo/Pict/rose.jpg'

# 開啟圖檔
with Image.open(file) as photo:
   # 方法crop()裁剪圖片
   img = photo.crop((312, 103, 918, 735))
   img.save('../Demo/Pict/cropRose.jpg')

# 開啟裁剪後圖片
file2 = '../Demo/Pict/cropRose.jpg'
with Image.open(file2) as photo:
   eff = photo.filter(ImageFilter.EDGE_ENHANCE_MORE)
   eff.save('../Demo/Pict/effRose.jpg')

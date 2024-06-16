# 方法blend()做照片合成, 兩張圖片的大小和格式要相同
from PIL import Image, ImageDraw, ImageFilter

#file = '../Demo/Pict/Rose.jpg'
file = 'Rose.jpg'
with Image.open(file) as photo:
   # 圖片裁切跟 lotus.jpg相同大小
   img = photo.resize((300, 225))
#   img.save('../Demo/Pict/rose2.jpg')
   img.save('rose2.jpg')

# s1 = Image.open('../Demo/Pict/lotus.jpg')
# s2 = Image.open('../Demo/Pict/rose2.jpg')

s1 = Image.open('lotus.jpg')
s2 = Image.open('rose2.jpg')

# 合成照片
target = Image.blend(s1, s2, alpha = 0.5)
#target.save('../Demo/Pict/show.jpg')
target.save('show.jpg')

# 方法new()產生灰階遮罩影像，大小須與s1, s2一樣
photo = Image.new("L", (300, 225))

# 產生橢圓遮罩區域
maskRect = ImageDraw.Draw(photo)
maskRect.ellipse((40, 40, 260, 220), fill = 255)

# 加入濾鐘鏡特為高斯模糊化
mask = photo.filter(ImageFilter.GaussianBlur(25))
#mask.save('../Demo/Pict/show2.jpg')
mask.save('show2.jpg')
#maskRect.show()

# 連同遮罩，做三張照片的合併
compImg = Image.composite(s1, s2, mask)
#compImg.save('../Demo/Pict/show3.png')
compImg.save('show3.png')
   
   

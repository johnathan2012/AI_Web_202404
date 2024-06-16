'''繪製橢圓圖案, 方法ellipse()在x、y座標(40, 50)
   產生一個寬、高為160 x 130的繪圖物件，
   以灰色填滿，外框為5的白色框線'''

from PIL import Image, ImageDraw, ImageFont

# 產生一個300X300灰色圖形
photo = Image.new('RGB', (300, 300), (215, 215, 215))
print('Px:', photo.getpixel((0, 0)))

# 產生繪圖物件
sample = ImageDraw.Draw(photo)

sample.ellipse((40, 50, 160, 130),
      fill = 'rgb(128, 128, 128)',
      outline = 'white', width = 5)
sample.ellipse((80, 70, 120, 110),
      fill = 'rgb(211, 211, 200)')

# 繪製弧線
sample.arc((15, 35, 180, 160), 180, 360, fill = 'DarkGray', width = 10)

# 取得字型
fontAt = ImageFont.truetype('../Demo/Font/BERNHC.ttf', 46)

# 繪圖物件繪製文字
sample.text((130, 120), 'Hi Pillow',
   font = fontAt, fill = 'Ivory')

# 儲存
photo.save('../Demo/Pict/1613.jpg')
photo.show()

from PIL import Image

file = '../Demo/Pict/004f.jpg'
with Image.open(file) as photo:
   print(photo.mode)
   # 變更為RGBA mode
   photo = photo.convert('RGBA')
   print(photo.mode)
   newLotus = []
   for item in photo.getdata():
      if item[:3] == (0, 163, 224):
         newLotus.append((255, 255, 255, 0))
      else:
         newLotus.append(item)
   photo.putdata(newLotus)
   photo.save('../Demo/Pict/1618.png')

from PIL import Image
from PIL import ImageDraw

img = Image.open("image.png")

I1 = ImageDraw.Draw(img)

I1.text((28, 36), "Sadettin Odabasi", fill=(255, 0, 0))

img.show()

img.save("image2.png")

from PIL import Image, ImageChops

im1 = Image.open("lemur.png", mode="r")
im2 = Image.open("flag.png", mode="r")

final = ImageChops.difference(im1,im2)

final.save("final.png")
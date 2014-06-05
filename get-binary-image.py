# get-binary-image.py
# Usage: python get-binary-image.py imagename color1 [color2, ...]
# 
# Makes a binary image from imagename where pixels matching any of the
# specified colors are black and all other pixels are white

from PIL import Image
import sys

path = sys.argv[1]
colors = map(int, sys.argv[2:])

im = Image.open(path)
im2 = Image.new("P", im.size, 255)
im = im.convert("P")

temp = {}

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        temp[pix] = pix
        if pix in colors:
            im2.putpixel((y,x),0)

#im2.save(path+"-binary.gif")
out = "binary"
for color in colors:
    out += "-" + str(color)
im2.save(out + ".gif")
            

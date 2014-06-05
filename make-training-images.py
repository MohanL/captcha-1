# make-training-images.py
# Usage: python make-training-images.py imagename outdirectory color [color2, ...]
#
# Makes vertical slice training images for imagename.
#
# imagename: The path to the image.
# outdirectory: The directory the training images should be placed in, without the trailing slash.
# color: The color of the text in the image. Multiple colors may be specified.

from PIL import Image
import hashlib
import sys

path = sys.argv[1]
out = sys.argv[2]
colors = map(int, sys.argv[3:])

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


inletter = False
foundletter = False
start = 0
end = 0

letters = []

for y in range(im2.size[0]): # slice across
    for x in range(im2.size[1]): # slice down
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True

    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))
    
    inletter=False


for letter in letters:
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    im3.save(out + "/" + hashlib.md5(im3.tostring()).hexdigest() + ".gif")

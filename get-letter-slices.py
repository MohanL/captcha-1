# get-letter-slices.py
# Usage: python get-letter-slices.py imagename color1 [color2, ...]
#
# Prints a list of tuples describing the start and end of every letter in an image

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

    inletter = False

print letters    

# crack.py
#
# Usage: python crack.py imagename color [color2, ...]

from PIL import Image
import hashlib
import sys
import os
import math

class VectorCompare:
    def magnitude(self,concordance):
        total = 0
        for word,count in concordance.iteritems():
            total += count ** 2
        return math.sqrt(total)

    def relation(self,concordance1,concordance2):
        relevance = 0
        topvalue = 0
        for word,count in concordance1.iteritems():
            if concordance2.has_key(word):
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


def buildvector(im):
    d1 = {}

    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1

    return d1

def main(args):
    v = VectorCompare()
    charset = ['2','3','4','5','6','7','8','9','b','c','d','f','g','h','j','k','m','n','p','q','r','s','t','v','w','x','y','z'] # No 0,1,a,e,i,l,o,u
    imageset = []

    for char in charset:
        for img in os.listdir("./training_set/%s/"%(char)):
            temp = []
            if img == "Thumbs.db": continue # Windows fix
            if img.startswith('.'): continue # ignore config files
            temp.append(buildvector(Image.open("./training_set/%s/%s"%(char,img))))
            imageset.append({char:temp})

    path = args[0]
    colors = map(int, args[1:])

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


    word = ""
    confidence = 1
    for letter in letters:
        im3 = im2.crop((letter[0],0,letter[1],im2.size[1]))
        guess = []
        for image in imageset:
            for x,y in image.iteritems():
                if len(y) != 0:
                    guess.append((v.relation(y[0],buildvector(im3)),x))

        guess.sort(reverse = True)
        confidence *= guess[0][0]
        word += str(guess[0][1])

    return (word,str(confidence))









# Make this script work from command line too
if __name__ == '__main__':
    print "{0[0]}  @  {0[1]}".format(main(sys.argv[1:]))

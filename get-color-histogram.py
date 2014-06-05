from PIL import Image
from operator import itemgetter
import sys


def hist(filename):
    im = Image.open(filename)
    im = im.convert("P")
    his = im.histogram()
    values = {}

    for i  in range(256):
        values[i] = his[i]

    print 'Color   Count'
    for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
        print '{0:>5}   {1}'.format(j,k)

    return


for arg in sys.argv[1:]:
    print '\n' + arg
    hist(arg)


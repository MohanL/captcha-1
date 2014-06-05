# count-training-images.py

from operator import itemgetter
import os

counts = []
for char in os.listdir("./training_set/"):
    if char == "index.php" or char.startswith('.'): continue;
    count = len(os.listdir("./training_set/%s/"%(char)))
    counts.append((char,count))


keysorted = sorted(counts)
valuesorted = sorted(counts,key=itemgetter(1),reverse=True)
print "Key-sorted         Value-sorted"
for i in range(len(counts)):
    print "'{0:s}' -> {1:<2d}          '{2:s}' -> {3:d}".format(keysorted[i][0],keysorted[i][1],valuesorted[i][0],valuesorted[i][1])

# crack-test.py
#
# Usage: python crack-test.py [-v]
#
# Options:
# -v    Print out the incorrect guesses

import sys
import os
import crack

options = sys.argv[1:]

solved = []
failed = []

totalattempts = 0
totalcorrect = 0
print "Suite      | Captchas | Correct | Percentage"
print "--------------------------------------------"
for suite in os.listdir("./test/"):
    if suite.startswith('.'): continue # ignore config files
    args = ''
    if os.path.isfile("test/%s/test-args.txt"%(suite)):
        f = open("./test/%s/test-args.txt"%(suite),'r')
        args = f.read()[:-1]
    attempts = 0
    correct = 0
    for img in os.listdir("./test/%s/"%(suite)):
        if img == 'index.php' or img == 'test-args.txt': continue
        guess = crack.main(("./test/%s/%s %s"%(suite,img,args)).split(' '))
        if img == guess[0]:
            solved.append(guess[0])
            correct += 1
        else:
            failed.append((guess,img))
        attempts += 1
    totalattempts += attempts
    totalcorrect += correct
    print "{0:10s} | {1:8d} | {2:7d} | {3:.2%}".format(suite,attempts,correct,float(correct)/float(attempts))
print "{0:10s} | {1:8d} | {2:7d} | {3:.2%}".format('Total',totalattempts,totalcorrect,float(totalcorrect)/float(totalattempts))

if '-v' in options:
    print "\n     ----- Incorrect Cracks ----- "
    print "{0:10s} | {1:12s} | {2:s}".format('Actual','Guess','Confidence')
    print "-----------|--------------|-----------"
    for x in failed:
        print "{0:10s} | {1:12s} | {2}".format(x[1],x[0][0],x[0][1])


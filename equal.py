import sys
import pickle


if len(sys.argv) != 3:
    print "usage: python unfinishedcentralcalc.py dist.pyfile path.pyfile songlist.pyfile"
    sys.exit()
user_input_1 = sys.argv[1]
user_input_2 = sys.argv[2]

picklefile = open(user_input_1, 'rb')
thing_1 = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input_2, 'rb')
thing_2 = pickle.load(picklefile)
picklefile.close()

print (thing_1 == thing_2)
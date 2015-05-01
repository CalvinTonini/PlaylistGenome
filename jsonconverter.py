import sys
import json
import pickle

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python jsonconverter.py file_name.json"
    sys.exit()

with open(user_input, mode = 'r') as f:
    variable = json.load(f)

output = user_input.replace(".json", ".pyfile")

outfile = open(output, 'wb')
pickle.dump(variable, outfile)
outfile.close()
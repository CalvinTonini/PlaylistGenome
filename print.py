# import collections
# import sys
# import pickle

# if len(sys.argv) == 4:
#     user_input = sys.argv[1]
#     user_input_1 = sys.argv[2]
#     user_input_2 = sys.argv[3]
# else:
#     print "usage: python unfinishedpathfinder.py [graph.pyfile]"
#     sys.exit()

# picklefile = open(user_input, 'rb')
# user_graph = pickle.load(picklefile)
# picklefile.close()

# for each in user_graph:
#     for every in each:
#         if each.count(every) > 1:
#             print every

lst = [1,2,3,4,2]

for each in lst:
    if lst.count(each) 
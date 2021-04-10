import sys

filename = sys.argv[1]
data  = sys.argv[2]

fh = open(filename,'a')

fh.write(data + "\n")

fh.close()
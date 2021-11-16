import sys

with open(sys.argv[1], "r") as fh:
    lines = fh.readlines ()
##This code will open a file for reading, which closes after the code line
##after it opens the file it will read all the lines
##for phyton we need 4 spaces on the next line after an ":"


for line in lines:
    print(len(line))



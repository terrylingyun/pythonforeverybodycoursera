fname = input('Enter a file name: ')
file = open(fname)
for line in file :
    line = line.upper()
    line = line.rstrip()
    print(line)

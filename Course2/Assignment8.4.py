fname = input('Enter a file name: ')
file = open(fname)
lst = list()
for line in file :
    oglst = line.split()
    for word in oglst :
        if not word in lst :
            lst.append(word)
lst.sort()
print(lst)

fname = input('Enter a file name: ')
file = open(fname)
count = 0
for line in file :
    if line.startswith('From:') :
        continue
    elif line.startswith('From') :
        lst = line.split()
        print(lst[1])
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')

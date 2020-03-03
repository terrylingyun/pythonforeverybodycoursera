fname = input('Enter a file name: ')
if len(fname) < 1 :
    fname = 'mbox-short.txt'
file = open(fname)
hours = dict()
for line in file :
    if line.startswith('From '):
        lst = line.split()
        lst = lst[5]
        lst = lst.split(':')
        hour = lst[0]
        hours[hour] = hours.get(hour, 0) + 1
hours_sort = sorted(hours.items())
for k,v in hours_sort :
    print(k,v)

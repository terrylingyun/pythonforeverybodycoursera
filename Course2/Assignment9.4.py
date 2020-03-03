fname = input('Enter a file name: ')
if len(fname) < 1 :
    fname = 'mbox-short.txt'
file = open(fname)
emails = dict()
emailmaxcount = 0
emailmax = None
for line in file :
    if line.startswith('From:') :
        continue
    elif line.startswith('From') :
        lst = line.split()
        email = lst[1]
        emails[email] = emails.get(email, 0) + 1
for address in emails :
    if emails[address] > emailmaxcount :
        emailmax = email
        emailmaxcount = emails[address]
print(emailmax, emailmaxcount)

fname = input('Enter a file name: ')
file = open(fname)
count = 0
spamtotal = 0.0
for line in file :
    if line.startswith('X-DSPAM-Confidence:') :
        count = count + 1
        spamposition = line.find(':')
        spam = line[spamposition+1:]
        spam = spam.lstrip()
        spam = float(spam)
        spamtotal = spamtotal + spam
        continue
print('Average spam confidence:',spamtotal/count)

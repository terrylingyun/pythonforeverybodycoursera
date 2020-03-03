import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
total = 0
print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
data = ET.fromstring(data)
data = data.findall('.//comment')
counts = list()
for item in data :
    counts.append(item.find('count').text)
print('Count:', len(counts))

total = 0
for count in counts :
    count = int(count)
    total = total + count
print('Sum:', total)
